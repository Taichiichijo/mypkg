import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "greeting", 10)
        self.create_timer(2.0, self.cb)
        self.messages = ["Hello", "Hi there!", "Good morning", "Howdy", "Hey!"]
        self.index = 0

    def cb(self):
        msg = String()
        msg.data = self.messages[self.index]
        self.get_logger().info(f"Talker says: {msg.data}")
        self.pub.publish(msg)
        self.index = (self.index + 1) % len(self.messages)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

i
if __name__ == "__main__":
    main()
