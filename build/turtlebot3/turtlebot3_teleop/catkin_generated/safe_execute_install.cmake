execute_process(COMMAND "/home/lip/robotics/ROS/atividades/atividades_22_04/atv3_ws/build/turtlebot3/turtlebot3_teleop/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/lip/robotics/ROS/atividades/atividades_22_04/atv3_ws/build/turtlebot3/turtlebot3_teleop/catkin_generated/python_distutils_install.sh) returned error code ")
endif()