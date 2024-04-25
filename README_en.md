<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# URG Node

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
    　<a href="#launch-and-usage">Launch and Usage</a>
    </li>
    <li><a href="#milestone">Milestone</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- INTRODUCTION -->
## Introduction

This repository is for launching Laser Range-Finders (LRF).
This repository contains a node that publishes sensor data from a Laser Range-Finder to the Robot Operating System (ROS). Developers working with ROS can use this node to connect a LRF to an existing ROS installation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This section describes how to set up this repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

First, please set up the following environment before proceeding to the next installation stage.

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| Python | 3.8 |
| Driver | SCIP 2.2 |

> [!NOTE]
> If you need to install `Ubuntu` or `ROS`, please check our [SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### Installation

1. Go to the `src` folder of ROS.
   ```sh
   $ roscd
   # Or just use "cd ~/catkin_ws/" and change directory.
   $ cd src/
   ```
2. Clone this repository.
   ```sh
   $ git clone https://github.com/TeamSOBITS/urg_node
   ```
3. Navigate into the repository.
   ```sh
   $ cd urg_node/
   ```
4. Install the dependent packages.
   ```sh
   $ bash install.sh
   ```
5. Compile the package.
   ```sh
   $ roscd
   # Or just use "cd ~/catkin_ws/" and change directory.
   $ catkin_make
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LAUNCH AND USAGE EXAMPLES -->
## Launch and Usage

1. Set the parameters inside [urg_lidar.launch](launch/urg_lidar.launch).
    ```xml
    <!-- If using LAN cable, set IP address -->
    <param name="ip_address" value=""/>
    <!-- If using USB cable, set serial configuration -->
    <param name="serial_port" value="/dev/ttyACM0"/>
    <param name="serial_baud" value="115200"/>
    ```

> [!NOTE]
> You can find the value of serial_port with `ls -la /dev/ttyACM*` command.

2. Execute the launch file [urg_lidar.launch](launch/urg_lidar.launch).
    ```sh
    $ roslaunch urg_node urg_lidar.launch
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MILESTONE -->
## Milestone

- [ ] TBD

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Reference

- [urg_node ROS Official Website](https://wiki.ros.org/urg_node)
- [HOKUYO Website](https://www.hokuyo-aut.co.jp/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TeamSOBITS/urg_node.svg?style=for-the-badge
[contributors-url]: https://github.com/TeamSOBITS/urg_node/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TeamSOBITS/urg_node.svg?style=for-the-badge
[forks-url]: https://github.com/TeamSOBITS/urg_node/network/members
[stars-shield]: https://img.shields.io/github/stars/TeamSOBITS/urg_node.svg?style=for-the-badge
[stars-url]: https://github.com/TeamSOBITS/urg_node/stargazers
[issues-shield]: https://img.shields.io/github/issues/TeamSOBITS/urg_node.svg?style=for-the-badge
[issues-url]: https://github.com/TeamSOBITS/urg_node/issues
[license-shield]: https://img.shields.io/github/license/TeamSOBITS/urg_node.svg?style=for-the-badge
[license-url]: LICENSE
