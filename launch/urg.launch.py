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
    launch_description = LaunchDescription([
        DeclareLaunchArgument(
            'config_file',
            default_value=os.path.join(get_package_share_directory('urg_node'), 'config', "urg_node_ethernet.yaml")
    )])

    use_namespace_cmd = DeclareLaunchArgument(
        'use_namespace',
        default_value='false'
    )

    namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='laser'
    )

    def expand_param_file_name(context):
        param_file = os.path.join(context.launch_configurations['config_file'])
        if os.path.exists(param_file):
            return [SetLaunchConfiguration('param', param_file)]

    param_file_path = OpaqueFunction(function=expand_param_file_name)

    hokuyo_node = Node(
        package='urg_node', executable='urg_node_driver', output='screen',
        parameters=[LaunchConfiguration('param')],
        condition=UnlessCondition(LaunchConfiguration('use_namespace'))
        )
    hokuyo_node_namespase = Node(
        package='urg_node', namespace=LaunchConfiguration('namespace'), executable='urg_node_driver', output='screen',
        parameters=[LaunchConfiguration('param')],
        condition=IfCondition(LaunchConfiguration('use_namespace'))
        )

    launch_description.add_action(param_file_path)
    launch_description.add_action(use_namespace_cmd)
    launch_description.add_action(namespace_cmd)
    launch_description.add_action(hokuyo_node)
    launch_description.add_action(hokuyo_node_namespase)
    return launch_description
