#!/bin/bash

echo "╔══╣ Install: URG Node (STARTING) ╠══╗"


# Install ROS packages
sudo apt-get update
sudo apt-get install -y \
    ros-${ROS_DISTRO}-urg-c


echo "╚══╣ Install: URG Node (FINISHED) ╠══╝"
