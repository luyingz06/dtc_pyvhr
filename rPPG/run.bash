#!/bin/bash


xhost +
docker run --rm -it --gpus all \
  --network=host \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v "/tmp/.X11-unix:/tmp/.X11-unix" \
  dtc-jackal-$(hostname | tr '[:upper:]' '[:lower:]'):rppg \
  bash