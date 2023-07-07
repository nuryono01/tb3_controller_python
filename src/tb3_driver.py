#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897


def move():
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(lin_speed)
    else:
        vel_msg.linear.x = -abs(lin_speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= lin_speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)
    



def rotate():
    #Converting from angles to radians
    angular_speed = deg_speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    

if __name__ == '__main__':
    try:
        #Testing our function
        rospy.init_node('tb3_driver', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        print("Inputting Linear&Angular Drive")
        lin_speed =float(input("Input your linear speed (m/sec):"))
        distance = float(input("Type your distance (m):"))
        isForward = bool(input("Foward?: "))#True or False
        deg_speed = float(input("Input your angular speed (degrees/sec):"))
        angle = float(input("Type your angle (degrees):"))
        clockwise = bool(input("Clockwise?: "))#True or false
        move()
        rotate()
        exit()

    except rospy.ROSInterruptException: pass
