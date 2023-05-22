import socket
import sys
import numpy as np
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from custom_interfaces.srv import SensorData

# requesting 2 samples on each call
number_of_samples = 2

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.3', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# Initialize a ROS node
rclpy.init()
node = rclpy.create_node('sensor_publisher')

# Create a publisher to publish the sensor data
publisher = node.create_publisher(Float64MultiArray, 'sensor_data', 10)

# Create a service client to call the custom service
client = node.create_client(SensorData, 'sensor_service')

# Callback function to print the received data
def sensor_data_callback(msg):
    print('Received sensor data:', msg.data)

# Subscribe to the sensor data topic
subscription = node.create_subscription(
    Float64MultiArray,
    'sensor_data',
    sensor_data_callback,
    10
)
subscription  # Prevent unused variable warning

while rclpy.ok():
    message_string = str(number_of_samples)
    message = message_string.encode()
    sock.sendall(message)

    byte_data = sock.recv(10000)
    data = np.frombuffer(byte_data)

    # Split the data array into xyz data for each sample
    split_data = np.split(data, number_of_samples)

    # Publish the first dataset as a topic
    msg1 = Float64MultiArray()
    msg1.data = split_data[0].tolist()
    publisher.publish(msg1)

    # Publish the second subarray as a topic
    msg2 = Float64MultiArray()
    msg2.data = split_data[1].tolist()
    publisher.publish(msg2)

    # Call the sensor service to process the data
    request = SensorData.Request()
    request.data = data.tolist()
    future = client.call_async(request)

    # Spin the node until the service call is completed
    rclpy.spin_once(node)

# Clean up the connection
print('closing socket')
sock.close()
