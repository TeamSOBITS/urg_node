<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# URG Node

<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#環境構築">環境構築</a>
      <ul>
        <li><a href="#環境条件">環境条件</a></li>
        <li><a href="#インストール方法">インストール方法</a></li>
      </ul>
    </li>
    <li>
    　<a href="#実行操作方法">実行・操作方法</a>
    </li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#参考文献">参考文献</a></li>
  </ol>
</details>



## 概要

Laser Range-Finders(LRF)を起動するためのレポジトリです．
本レポジトリは，LRFからセンサーデータをRobot Operating System (ROS)にパブリッシュするノードです．ROSで作業している開発者は，このノードを使用してLRFを既存のROSインストールに接続できます．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- セットアップ -->
## セットアップ

ここで，本レポジトリのセットアップ方法について説明します．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### 環境条件

まず，以下の環境を整えてから，次のインストール段階に進んでください．

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| Python | 3.8 |
| Driver | SCIP 2.2 |

> [!NOTE]
> `Ubuntu`や`ROS`のインストール方法に関しては，[SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)に参照してください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### インストール方法

1. ROSの`src`フォルダに移動します．
   ```sh
   $ roscd
   # もしくは，"cd ~/catkin_ws/"へ移動．
   $ cd src/
   ```
2. 本レポジトリをcloneします．
   ```sh
   $ git clone https://github.com/TeamSOBITS/urg_node
   ```
3. レポジトリの中へ移動します．
   ```sh
   $ cd urg_node/
   ```
4. 依存パッケージをインストールします．
   ```sh
   $ bash install.sh
   ```
5. パッケージをコンパイルします．
   ```sh
   $ roscd
   # もしくは，"cd ~/catkin_ws/"へ移動．
   $ catkin_make
   ```

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


## 実行・操作方法

1. URG LiDARの[urg_lidar.launch](launch/urg_lidar.launch)にあるパラメータを設定する．
    ```xml
    <!-- If using LAN cable, set IP address -->
    <param name="ip_address" value=""/>
    <!-- If using USB cable, set serial configuration -->
    <param name="serial_port" value="/dev/ttyACM0"/>
    <param name="serial_baud" value="115200"/>
    ```

> [!NOTE]
> serial_portのvalueの値を確認するには，`ls -la /dev/ttyACM*`を実行してください．

2. [urg_lidar.launch](launch/urg_lidar.launch)というlaunchファイルを実行する．
    ```sh
    $ roslaunch urg_node urg_lidar.launch
    ```

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### Publisher

| Topic Name | Type | Meaning |
| --- | --- | --- |
| /scan | sensor_msgs/LaserScan | Scan result from URG |

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- マイルストーン -->
## マイルストーン

- [ ] TBD

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- 参考文献 -->
## 参考文献

- [urg_node ROS公式サイト](https://wiki.ros.org/urg_node)
- [HOKUYOサイト](https://www.hokuyo-aut.co.jp/)

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>



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
