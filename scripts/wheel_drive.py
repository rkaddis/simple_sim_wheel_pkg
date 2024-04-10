#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from simple_sim_wheel_pkg.cfg import SimWheelConfig
from dynamic_reconfigure.server import Server

twist_msg = Twist()
twist_msg.linear.x = 0
twist_msg.angular.z = 0

def dyn_rcfg_cb(config, level):
    global max_steer, max_speed, max_accel, max_decel
    max_steer = config.max_steer
    max_speed = config.max_speed
    max_accel = config.max_accel
    max_decel = config.max_decel
    return config


def wheel_cb(msg):

    wheel_input = msg.axes[0] #steering wheel axis input
    gas_input = (msg.axes[1] + 1) / 2 #gas pedal axis input
    brake_input = (msg.axes[2] + 1) / 2  #brake pedal axis input

    twist_msg.angular.z = wheel_input * max_steer
    #print(gas_input, brake_input)
    if(brake_input > 0): #braking
        #print("brake")
        if(twist_msg.linear.x <= 0.02 * max_speed):
            twist_msg.linear.x = 0
        else:
            twist_msg.linear.x -= twist_msg.linear.x * max_decel * brake_input
    
    elif(gas_input > 0): #accelerating
        #print("gas")
        if(twist_msg.linear.x >= max_speed):
            twist_msg.linear.x = max_speed
        else:
            twist_msg.linear.x += twist_msg.linear.x * max_accel * gas_input
            

    else: #coasting
        if(twist_msg.linear.x <= 0):
            twist_msg.linear.x = 0.1
        else:
            twist_msg.linear.x -= twist_msg.linear.x * max_decel * 0.1

    vel_pub.publish(twist_msg)

    

if __name__ == '__main__':

    rospy.init_node('wheel_drive', anonymous=True)

    vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('joy', Joy, wheel_cb, queue_size=1)
    srv = Server(SimWheelConfig, dyn_rcfg_cb)

    rospy.spin()

    


