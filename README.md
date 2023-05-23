# Robotic Homework Solution
## Introduction
The goal of this project was to build a ROS2 network that will handle data from a 3 degree of freedom (3 DOF) sensor. A simple sensor simulator from the provided sensor.py file was used to generate random data mimicking a real sensor. The project's solution uses a service and client package to manage the data. The service reads data from 2 variations of the simulated sensor, and sends that data to the client. The client connects to the server to obtain sensor data and publishes it to a topic. The topic is then subscribed to in order to print the topic on the command line. The resulting output is xyz data for each sensor being printed on the client’s command line at a rate of 500 Hz.

## Installation and Usage
To use this repository, ROS2 should be installed (the Humble distribution was used to develop this code). With ROS2 installed, follow these steps to implement the repository:
1.  Clone the repository by running the following command in a terminal
	```git clone https://github.com/jessicaanz/Machina_Robotics_HW.git```
2. Navigate to the ‘ros2_ws’ directory, check for missing dependencies, and build the workspace
	‘cd ros2_ws’
	‘rosdep install -i --from-path src --rosdistro humble -y’
	‘colcon build’
3. Open a new terminal, navigate to the workspace, and source the setup files
	‘cd ros2_ws’
	‘source install/setup.bash’
4. Run the service node
	‘ros2 run sensor_data service’
5. Open another terminal, navigate to the workspace, and source the setup files (repeat step 3)
6. Run the client node
	‘ros2 run sensor_data client’
The client node should now print data for each sensor to the command line.

## Chosen Number of Samples
Calls to the sensors should be published at a rate of 500 Hz, which means each call should take 2 ms total. The first sensor has a 2000 Hz sampling rate and a 1 ms delay. This sensor takes 0.5ms per sample, plus the 1 ms delay time. Therefore, 2 samples should be taken so that the total call time is the desired 2 ms. The second sensor has a 4000 Hz sampling rate and a 1 ms delay. This sensor takes 0.25ms per sample, plus the 1 ms delay. Therefore, 4 samples should be taken to achieve the desired 2 ms call time.

## Sources
- Machina Labs Robotic Homework Repository: [https://github.com/Machina-Labs/robotic_hw](https://github.com/Machina-Labs/robotic_hw)
- ROS2 Documentation: Humble Tutorials: [https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)
- Foxglove Creating ROS2 Services [https://foxglove.dev/blog/creating-ros2-services](https://foxglove.dev/blog/creating-ros2-services)
- Robotics Backend ROS2 Tutorial 11 [https://youtu.be/vCTbUgw6k8U](https://youtu.be/vCTbUgw6k8U)
