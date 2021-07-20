# Copyright (c) 2020 AIST.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""A service that publishes a test message when called."""

from publisher_service_msgs.srv import PublishService

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PublisherService(Node):
    """Publisher service node."""

    def __init__(self):
        """Initialize."""
        super().__init__('publisher_service')
        self.publisher_ = self.create_publisher(String, 'test_topic', 10)
        self.service_ = self.create_service(
            PublishService, 'publish_msg', self.publish_callback)

    def publish_callback(self, request, response):
        """Publish a message."""
        msg = String()
        msg.data = request.msg
        self.publisher_.publish(msg)
        return response


def main(args=None):
    """Initialize ROS and the publisher service."""
    rclpy.init(args=args)
    publisher_service = PublisherService()

    rclpy.spin(publisher_service)

    publisher_service.destroy_node()

    rclpy.shutdown()
