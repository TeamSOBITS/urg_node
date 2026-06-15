import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction
from launch.actions import SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

from launch_ros.actions import Node


def _bool(val):
    return val.lower() in ('true', '1', 'yes')


def _expand_param_file_name(context):
    param_file = context.launch_configurations['config_file']
    if os.path.exists(param_file):
        return [SetLaunchConfiguration('param', param_file)]


def _make_nodes(context):
    namespace = context.launch_configurations['namespace']
    laser_frame_id = context.launch_configurations['laser_frame_id']
    enable_tf_prefix = _bool(context.launch_configurations['enable_tf_prefix'])
    use_namespace = _bool(context.launch_configurations['use_namespace'])

    extra_params = []
    if enable_tf_prefix:
        extra_params.append({'laser_frame_id': namespace + '/' + laser_frame_id})

    common_params = [LaunchConfiguration('param')] + extra_params

    if not use_namespace:
        return [Node(
            package='urg_node', executable='urg_node_driver', output='screen',
            parameters=common_params,
        )]
    else:
        return [Node(
            package='urg_node', namespace=namespace, executable='urg_node_driver', output='screen',
            parameters=common_params,
        )]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'config_file',
            default_value=os.path.join(get_package_share_directory('urg_node'), 'config', "urg_node_ethernet.yaml")
        ),
        DeclareLaunchArgument('use_namespace', default_value='false'),
        DeclareLaunchArgument('namespace', default_value='laser'),
        DeclareLaunchArgument('enable_tf_prefix', default_value='false'),
        DeclareLaunchArgument('laser_frame_id', default_value='laser'),
        OpaqueFunction(function=_expand_param_file_name),
        OpaqueFunction(function=_make_nodes),
    ])
