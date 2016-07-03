import rosbag
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
bridge = CvBridge()

bag=rosbag.Bag('sensor_car.rosbag.QQ39P0.1.1464256647.0.bag')
for msg in bag.read_messages():
    filename = str(msg.message.header.seq) + '.bmp';
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg.message, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        cv2.imwrite(filename, cv2_img)
