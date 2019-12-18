#!/usr/bin/env python
import rospy

from std_msgs.msg import Bool



def blink():

    pub = rospy.Publisher('led_blink', Bool, queue_size=10)

    rospy.init_node('blink1_led', anonymous=True)

    r = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        button = "1 %d"%rospy.get_time()

        pub.publish(1)
        rospy.sleep(1.0)
        pub.publish(0)
        rospy.sleep(1.0)

             

if __name__ == '__main__':

    try:

        blink()

    except rospy.ROSInterruptException: pass