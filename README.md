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

Test on existing data using pyvhr pipeline and give estimated results vs ground truth (Nov. 20th - Nov. 24th).

Utilize deep learning model after the image preprocess (skin extraction) and get results (Nov. 24th - Nov. 28th).

Train new deep neural network models (Further schedule).
