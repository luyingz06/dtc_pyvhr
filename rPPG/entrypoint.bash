#!/bin/bash

source /opt/ros/noetic/setup.bash
source ws/devel/setup.bash
if [ "$RUN" = true ]; then
    echo "[rPPG] Launching rPPG Network"
    roslaunch rppg_ros rppg.launch --wait
else
    echo "[rPPG] RUN set to false, not rPPG Network"
fi
