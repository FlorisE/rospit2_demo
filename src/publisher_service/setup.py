"""Setup script for publisher_service."""

from setuptools import setup

package_name = 'publisher_service'

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
    maintainer='floris',
    maintainer_email='floris.erich@aist.go.jp',
    description='Package that contains service that can publish messages.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_service = publisher_service.publisher_service:main',
        ],
    },
)
