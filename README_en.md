<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

# urg_node

## Introduction
This repository is for launching Laser Range-Finders (LRF).
This repository contains a node that publishes sensor data from a Laser Range-Finder to the Robot Operating System (ROS). Developers working with ROS can use this node to connect a LRF to an existing ROS installation.

## Supported Hardware
This driver works with any SCIP 2.2 or earlier compliant laser range-finders.

## Environments
- OS : Ubuntu 20.04
- ROS distribution : Noetic Ninjemys

## Installation
```bash
# Move to catkin_ws/src
$ cd ~/catkin_ws/src
# Clone this package
$ git clone https://github.com/TeamSOBITS/urg_node.git
# Build the package
$ cd ~/catkin_ws && catkin_make
```

## How to use
```
$ roslaunch urg_node urg_lidar.launch
```

## Caution
- Modify the value of serial_port in the launch file according to the LiDAR you are using.
```bash
<param name="serial_port" value="/dev/ttyACM0"/>
```
To find the value of serial_port:
```bash
$ ls -la /dev/ttyACM*
```
## Reference
- [ROS Official Website](https://wiki.ros.org/urg_node)

<p align="right">(<a href="#readme-top">back to top</a>)</p>