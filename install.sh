#!/bin/bash

echo "╔══╣ Install: URG Node (STARTING) ╠══╗"


# Install ROS packages
sudo apt-get update
sudo apt-get install -y \
    ros-${ROS_DISTRO}-urg-c \
    ros-${ROS_DISTRO}-laser-proc \
    ros-${ROS_DISTRO}-urg-node-msgs
    ros-${ROS_DISTRO}-rosidl-typesupport-c



echo "╚══╣ Install: URG Node (FINISHED) ╠══╝"