# ROS turtle control

Start:

```bash
cd ~/catkin_ws
mkdir images_posting

catkin_create_pkg images_posting image_transport cv_bridge sensor_msgs rospy roscpp std_msgs
mv <this_project> images_posting
catkin_make

roscd images_posting
roslaunch images_posting images_posting.launch
```
