# SPDX-FileCopyrightTest: 2024 Taichi Ichijo
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class GreetingNode(Node):
    def __init__(self):
        super().__init__("greeting_node")
        self.pub = self.create_publisher(String, "greeting", 10)
        self.create_timer(2.0, self.cb)
        self.messages = ["Hello", "Hi there!", "Good morning", "Howdy", "Hey!"]
        self.index = 0

    def cb(self):
        msg = String()
        msg.data = self.messages[self.index]
        self.pub.publish(msg)
        self.index = (self.index + 1) % len(self.messages)

def main():
    rclpy.init()
    node = GreetingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
