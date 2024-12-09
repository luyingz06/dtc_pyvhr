#!/bin/bash


xhost +
docker run --rm -it --gpus all \
  --network=host \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v "/tmp/.X11-unix:/tmp/.X11-unix" \
  -v "/home/luying/dtc_pyvhr/rPPG/configs:/home/`whoami`/configs" \
  -v "/home/luying/dtc_pyvhr/rPPG/loss:/home/`whoami`/loss" \
  -v "/home/luying/dtc_pyvhr/rPPG/train:/home/`whoami`/train" \
  -v "/home/luying/dtc_pyvhr/rPPG/rppg_ros:/home/`whoami`/ws/src/rppg_ros" \
  -v "/home/luying/dtc_pyvhr/rPPG/output:/home/`whoami`/videos" \
  dtc-jackal-$(hostname | tr '[:upper:]' '[:lower:]'):rppg \
  bash