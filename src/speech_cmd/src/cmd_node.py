import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class voiceCMD:
    def __init__(self):
        #rospy.init_node('cmd_ctrl_node', anonymous=False)
        self.text_cmd_ = rospy.Subscriber("robot/voicecontrol/commands", String, self.checkCMD, queue_size = 10)
        self.robot_cmd_ = rospy.Publisher("cmd_vel", Twist, queue_size = 10)
        self.data_cmd_ = Twist()
    
    def checkCMD(self, msg):
        command = self.text_cmd_
        command2 = msg.data
        if "foward" in command2.lower():
            self.data_cmd_.linear.x = 0.1
            self.data_cmd_.angular.z = 0.0        
            pass
        elif "left" in command2.lower():
            self.data_cmd_.linear.x = 0.0
            self.data_cmd_.angular.z = -0.1
            pass
        elif "right" in command2.lower():
            self.data_cmd_.linear.x = 0.0
            self.data_cmd_.angular.z = 0.1
            pass
        elif "back" in command2.lower():
            pass
        elif "die" in command2.lower():
            pass
        elif "kill" in command2.lower():
            pass
        pass

        self.robot_cmd_.publish(self.data_cmd_)


if __name__ == '__main__':
    try:
        rospy.init_node('cmd_ctrl_node', anonymous=False)
        v_cmd = voiceCMD()

        while not rospy.is_shutdown():
            rospy.spin()

        pass
    except rospy.ROSInterruptEcxeption:
        pass


