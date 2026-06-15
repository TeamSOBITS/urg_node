import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction
from launch.actions import SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

from launch_ros.actions import Node


def generate_launch_description():
    launch_description = LaunchDescription()

    namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='laser'
    )

    lidar_num_cmd = DeclareLaunchArgument(
        'lidar_num',
        default_value='2'
    )

    enable_tf_prefix_cmd = DeclareLaunchArgument(
        'enable_tf_prefix',
        default_value='false'
    )

    launch_description.add_action(namespace_cmd)
    launch_description.add_action(lidar_num_cmd)
    launch_description.add_action(enable_tf_prefix_cmd)
    launch_description.add_action(OpaqueFunction(function = multi_param_launch))
    return launch_description


def _bool(val):
    return val.lower() in ('true', '1', 'yes')


def multi_param_launch(context, *args, **kwargs):
    namespace = LaunchConfiguration('namespace').perform(context)
    lidar_num = LaunchConfiguration('lidar_num').perform(context)

    config_files_cmd = []
    topic_namespaces_cmd = []
    for i in range(int(lidar_num)):
        config_files_cmd += [DeclareLaunchArgument('config_file' + str(i+1), default_value=os.path.join(get_package_share_directory('urg_node'), 'config', "urg_node_multi_ethernet" + str(i+1) + ".yaml"))]
        topic_namespaces_cmd += [DeclareLaunchArgument('topic_namespace' + str(i+1), default_value="lidar" + str(i+1))]

    return config_files_cmd + topic_namespaces_cmd + [OpaqueFunction(function = multi_node_launch)]


def multi_node_launch(context, *args, **kwargs):
    namespace = LaunchConfiguration('namespace').perform(context)
    lidar_num = LaunchConfiguration('lidar_num').perform(context)
    enable_tf_prefix = _bool(LaunchConfiguration('enable_tf_prefix').perform(context))

    topic_namespaces = []
    for i in range(int(lidar_num)):
        topic_namespaces += [LaunchConfiguration('topic_namespace' + str(i+1)).perform(context)]

    node_list = []
    for i in range(int(lidar_num)):
        params = [LaunchConfiguration('config_file' + str(i+1))]
        if enable_tf_prefix:
            params.append({'laser_frame_id': namespace + '/' + topic_namespaces[i] + '_laser'})
        node_list += [Node(
            package='urg_node', namespace=namespace, executable='urg_node_driver', name='urg_node'+str(i+1), output='screen',
            remappings=[('/' + namespace + '/scan', '/' + namespace + '/' + topic_namespaces[i] + '/scan')],
            parameters=params,
        )]

    return node_list