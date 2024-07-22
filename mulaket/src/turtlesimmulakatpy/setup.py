from setuptools import find_packages, setup

package_name = 'turtlesimmulakatpy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yusufkaratas231998',
    maintainer_email='yusufkaratas231998@email.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = turtlesimmulakatpy.publisher_member_function:main',
            'server = turtlesimmulakatpy.createturtlesim:main',
            'cleint = turtlesimmulakatpy.createturtlesimclient:main',
            'turtlespawner = turtlesimmulakatpy.turtle:main'
            
        ],
    },
)
