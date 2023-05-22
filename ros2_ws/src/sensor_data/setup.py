from setuptools import setup

package_name = 'sensor_data'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jessica Anz',
    maintainer_email='jca54@duke.edu',
    description='Service and client to publish data for 3 DOF sensor.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'service = sensor_data.sensor_service:main',
          'client = sensor_data.sensor_client:main',
        ],
    },
)
