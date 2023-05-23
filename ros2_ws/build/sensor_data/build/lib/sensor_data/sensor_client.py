# Based on example.py
# Import needed libraries and modules
import socket
import sys
import numpy as np
import time
import rclpy
# Import msg and srv files
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from custom_interfaces.srv import SensorData

# Define sample request for each sensor
number_of_samples1 = 2
number_of_samples2 = 2

# Create a TCP/IP socket for each sensor
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the sockets to the ports where the servers are listening
server_address1 = ('127.0.0.3', 10000)  # Server address for sensor 1
server_address2 = ('127.0.0.1', 10000)  # Server address for sensor 2
print('connecting to {} port {}'.format(*server_address1))
print('connecting to {} port {}'.format(*server_address2))
sock1.connect(server_address1)
sock2.connect(server_address2)

# Initialize a ROS node for the publishing and subscribing
rclpy.init()
node = rclpy.create_node('sensor_publisher')

# Create publishers to publish the sensor data for each sensor
publisher1 = node.create_publisher(Float64MultiArray, 'sensor_data1', 10)
publisher2 = node.create_publisher(Float64MultiArray, 'sensor_data2', 10)

# Create service clients to call the custom service for each sensor
client1 = node.create_client(SensorData, 'sensor_service1')
client2 = node.create_client(SensorData, 'sensor_service2')

# Callback functions to print the received data
def sensor_data_callback1(msg):
    print('Sensor 1:', msg.data)
def sensor_data_callback2(msg):
    print('Sensor 2:', msg.data)

# Create subscribers to the sensor data topics
subscription1 = node.create_subscription(
    Float64MultiArray,
    'sensor_data1',
    sensor_data_callback1,
    10
)
subscription2 = node.create_subscription(
    Float64MultiArray,
    'sensor_data2',
    sensor_data_callback2,
    10
)
subscription1
subscription2  # Prevent unused variable warnings

# While loop to run as long as the ROS2 network runs
while rclpy.ok():
    # Retrieve data from sensor 1
    message_string = str(number_of_samples1)
    message = message_string.encode()
    sock1.sendall(message)
    byte_data1 = sock1.recv(10000)
    # Gives array of data from the called samples
    data1 = np.frombuffer(byte_data1)

    # Split the data array into xyz data for each sample
    split_data1 = np.split(data1, number_of_samples1)

    # Publish the first dataset from sensor 1 as a topic
    msg1 = Float64MultiArray()
    msg1.data = split_data1[0].tolist()
    publisher1.publish(msg1)

    # Publish the second subarray from sensor 1 as a topic
    msg2 = Float64MultiArray()
    msg2.data = split_data1[1].tolist()
    publisher1.publish(msg2)

    # Call the sensor service for sensor 1 to process the data
    request1 = SensorData.Request()
    request1.data = data1.tolist()
    future1 = client1.call_async(request1)

    # Retrieve data from sensor 2
    message_string = str(number_of_samples2)
    message = message_string.encode()
    sock2.sendall(message)
    byte_data2 = sock2.recv(10000)
    data2 = np.frombuffer(byte_data2)

    # Split the data array into xyz data for each sample
    split_data2 = np.split(data2, number_of_samples2)

    # Publish the first dataset from sensor 2 as a topic
    msg3 = Float64MultiArray()
    msg3.data = split_data2[0].tolist()
    publisher2.publish(msg3)

    # Publish the second subarray from sensor 2 as a topic
    msg4 = Float64MultiArray()
    msg4.data = split_data2[1].tolist()
    publisher2.publish(msg4)

    # Call the sensor service for sensor 2 to process the data
    request2 = SensorData.Request()
    request2.data = data2.tolist()
    future2 = client2.call_async(request2)

    # Spin the node until the service calls are completed
    rclpy.spin_once(node)

# Clean up the connections
print('closing sockets')
sock1.close()
sock2.close()

