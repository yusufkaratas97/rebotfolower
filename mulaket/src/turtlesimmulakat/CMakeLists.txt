cmake_minimum_required(VERSION 3.8)
project(turtlesimmulakat)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(turtlesimmulakat REQUIRED)  

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Turtlescreate.srv"
  DEPENDENCIES geometry_msgs rclcpp # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)


add_executable(teleop_turtle_key src/teleop_turtle_key.cpp)
ament_target_dependencies(teleop_turtle_key geometry_msgs rclcpp std_msgs)

add_executable(turtles_create src/turtle_create.cpp)
ament_target_dependencies(turtles_create rclcpp)

install(TARGETS
  teleop_turtle_key
  DESTINATION lib/${PROJECT_NAME})


ament_package()



