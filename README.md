<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

# urg_node

## 概要
Laser Range-Finders(LRF)を起動するためのレポジトリです．
本レポジトリは，LRFからセンサーデータをRobot Operating System (ROS)にパブリッシュするノードです．ROSで作業している開発者は，このノードを使用してLRFを既存のROSインストールに接続できます．

## 対応ハードウェア
本ドライバは，SCIP 2.2またはそれ以前の規格に準拠したレーザー距離計で動作します．

## 環境
- OS : Ubuntu 20.04
- ROS version : Noetic Ninjemys

## インストール方法
```bash
# catkin_ws/srcに移動します
$ cd ~/catkin_ws/src
# 本パッケージをgit cloneします
$ git clone https://github.com/TeamSOBITS/urg_node.git
# パッケージのbuildをします
$ cd ~/catkin_ws && catkin_make
```

## 実行・操作方法
```
$ roslaunch urg_node urg_lidar.launch
```

## 注意事項
- 使用するLiDARに合わせてlaunchファイルの以下のserial_portのvalueの値を変更してください
```bash
<param name="serial_port" value="/dev/ttyACM0"/>
```
serial_portのvalueの値を確認する方法
```bash
$ ls -la /dev/ttyACM*
```
## 参考文献
- [ROS公式サイト](https://wiki.ros.org/urg_node)

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>