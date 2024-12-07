#!/usr/bin/python3
"""
    Aurora Zhang
    December 2024
    
    This is the ros node for rppg heart rate estimation
    It takes in masked frames from rosbags and then process through the network and return rPPG value.
"""

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge 

class rPPG:
    def __init(self):
        
