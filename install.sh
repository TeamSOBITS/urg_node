#!/bin/bash

echo "╔══╣ Install: URG Node (STARTING) ╠══╗"


# Install ROS packages
sudo apt-get update
sudo apt-get install -y \
    ros-${ROS_DISTRO}-urg-c \
    ros-${ROS_DISTRO}-laser-proc


echo "╚══╣ Install: URG Node (FINISHED) ╠══╝"
