#include "rclcpp/rclcpp.hpp"
//#include "turtlesimmulakat/srv/turtlescreate.hpp"

#include <memory>

void add()
{
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("turtles_create servar");

  

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "turtlecrates");

  rclcpp::spin(node);
  rclcpp::shutdown();
}