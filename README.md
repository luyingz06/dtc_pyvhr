# dtc_pyvhr

This is the virtual heart rate detection code for DARPA Triage Challenge (Team Pronto).

There are three nodes included in this repo, pyvhr, yolov9-ros, and mtts-can.

### yolov8_ros

This is a preprocess node that crops out the person in the image and return a smaller image that only contains the person body with background set to black.

### pyVHR

This is the conventional computation of heart rate using model-based method CHROM.
It analyzes the color signals in G channel (from RGB camera) and calculate BVP and BPM.
Return heart rate as an integer.

### mtts_can

This is the deep learning model for heart rate estimation.
It takes in frames and return heart rate as an integer.

# How to run


The code are locally on lml2 machine.

For **yolov8**, go to yolov8-ros and run ```./run.bash```. in container, run:
```
cd /ws
catkin build
source devel/setup.bash
roscore
rosbag play -l xx.bag #this is usually in pyvhr container
roslaunch yolov8_ros mask.launch
```

For **pyVHR**, go to /home/luying/Docker and run ```./run.bash``` to join the docker container, then run the following command:
```
cd pyvhr_ws
source devel/setup.bash
```

Then tmux and run following command:
```
rosbag play -l xx.bag #this is usually in pyvhr container
rosrun pyvhr pyvhr_node.py #initializa pyvhr node
```

For **mtts_can**, run ```./run.bash``` and go to container, tmux:
```
source devel/setup.bash
rosrun mtts_can_ros predict_ros.py # or roslaunch
rostopic pub /jackal_teleop/trigger std_msgs/UInt8 "data: 1"
rostopic echo /heart_rate/model
```


## Todo

√ Test on existing data using pyvhr pipeline and give estimated results vs ground truth (Nov. 20th - Nov. 24th). 

√ Test MTTS_CAN without preprocessing on the existing data and get comparison plots (Nov. 24th - Nov. 28th).

Evaluate MTTS_CAN or other deep learning models after the image preprocess (skin extraction) and get comparison results. (Dec. 2nd - Dec. 7th)

Train on new deep neural network models with image preprocess (Dec. 7th - Dec. 13th).

## Visualization

This is the visualization on 2024_10_18, 2024_10_24, and part of 2024_10_29 data:
![Figure_1](https://github.com/user-attachments/assets/5537b923-82dc-466d-8f88-f3a8a6682cb4)

And I also plotted the high heart rate (>85bpm) below:

![Figure_2](https://github.com/user-attachments/assets/e46cec89-5dce-4998-b79f-470a98caa942)

We can see that in general, the pyVHR shows a high variance and the performance is not very stable, while MTTS_CAN is more stable but it fails to detetct high heart rate.
