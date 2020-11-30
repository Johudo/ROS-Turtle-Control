#!/usr/bin/env python

import rospy
import commands

from geometry_msgs.msg import Twist



def create_turtle_log_msg (speed, rotation):
    return '''linear: 
    x: {}
    y: 0.0
    z: 0.0
angular:
    x: 0.0
    y: 0.0
    z: {}'''.format(speed, rotation)



def turtle_publisher(commands):
    pub = rospy.Publisher('turtle1/cmd_vel', Twist)
    rate = rospy.Rate(0.9)

    msg_to_publish = Twist()

    counter = 0

    while not rospy.is_shutdown():
        speed = commands[counter].get('speed')
        rotation = commands[counter].get('rotation')

        msg_to_publish.linear.x = speed
        msg_to_publish.angular.z = rotation

        pub.publish(msg_to_publish)

        data_to_publish = create_turtle_log_msg(speed,rotation)
        rospy.loginfo(data_to_publish)
        
        counter += 1 

        if counter == len(commands):
            counter = 0

        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('turtle_mai_node')
    
    turtle_publisher(commands.commands_list)
