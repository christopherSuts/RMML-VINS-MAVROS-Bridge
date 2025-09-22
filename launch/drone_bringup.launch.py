import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Mencari path ke file konfigurasi default dari MAVROS
    mavros_pkg_path = get_package_share_directory('mavros')
    apm_pluginlists_yaml = os.path.join(mavros_pkg_path, 'launch', 'apm_pluginlists.yaml')
    apm_config_yaml = os.path.join(mavros_pkg_path, 'launch', 'apm_config.yaml')

    # Mendefinisikan node MAVROS secara langsung
    mavros_node = Node(
        package='mavros',
        executable='mavros_node',
        namespace='mavros',
        output='screen',
        parameters=[
            # Memuat file pluginlist dan config default dari MAVROS
            apm_pluginlists_yaml,
            apm_config_yaml,
            # Menimpa (override) parameter fcu_url dengan nilai spesifik Anda
            {
                'fcu_url': '/dev/ttyACM0:921600'
            }
        ],
        # Menambahkan remapping odometry Anda di sini
        remappings=[
            # ('odometry/in', '/odometry')
            ('odometry/out', '/odometry')
        ]
    )

    return LaunchDescription([
        # Anda bisa menambahkan node VINS dan DepthAI Anda di sini juga
        mavros_node
    ])