import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "greeting", self.cb, 10)
        self.responses = [
            "Hi there!",
            "Hello!",
            "Nice to see you!",
            "Howdy!",
            "Hey, what's up?",
            "Good to hear from you!"
        ]

    def cb(self, msg):
        self.get_logger().info(f"Listener received: {msg.data}")
        response = random.choice(self.responses)
        self.get_logger().info(f"Listener responds: {response}")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
i    main()
