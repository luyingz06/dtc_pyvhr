# Base image with PyTorch and CUDA 12.1
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu20.04

# Set up timezone and locales
ENV TZ="America/New_York"
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    tzdata locales keyboard-configuration \
 && ln -fs "/usr/share/zoneinfo/$TZ" /etc/localtime \
 && dpkg-reconfigure --frontend noninteractive tzdata \
 && locale-gen en_US.UTF-8 \
 && apt-get clean

# Set locale environment variables
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en

# Install system dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    vim tmux cmake gcc g++ git build-essential sudo wget curl zip unzip libgl1-mesa-dri libgl1 \
    lsb-release \
 && apt-get clean

# Add a user
ARG user_id=1000
ARG USER=dtc
RUN useradd -U --uid ${user_id} -ms /bin/bash $USER \
 && echo "$USER:$USER" | chpasswd \
 && adduser $USER sudo \
 && echo "$USER ALL=NOPASSWD: ALL" >> /etc/sudoers.d/$USER

USER $USER
WORKDIR /home/$USER
COPY .bashrc .

# Install Python and upgrade pip
RUN sudo apt-get update \
 && sudo apt-get install -y python3 python3-pip \
 && sudo pip3 install --upgrade pip setuptools \
 && pip3 install --upgrade importlib_metadata 
# Install PyTorch with CUDA 12.1
RUN pip3 install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121

# Install ROS Noetic
RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \ && sudo /bin/sh -c 'curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -' \
 && sudo apt-get update \
 && sudo apt-get install -y \
    python3-catkin-tools \
    python3-rosdep \
    python3-rosinstall \
    ros-noetic-desktop-full

RUN sudo rosdep init \
 && sudo apt-get clean

RUN rosdep update

# Install Python libraries
RUN pip3 install opencv-python scipy matplotlib scikit-image

# Workspace setup
RUN mkdir -p ws/src

COPY ./entrypoint.bash entrypoint.bash
COPY ./rppg_ros ./ws/src/rppg_ros
COPY ./requirements.txt ./ws/requirements.txt
RUN pip3 install -r ./ws/requirements.txt

# setup environment
ARG NAME
ENV ROBOT=$NAME
RUN sudo chown $USER:$USER ~/.bashrc \
 && /bin/sh -c 'echo ". /opt/ros/noetic/setup.bash" >> ~/.bashrc' \
 && /bin/sh -c 'echo "source ~/ws/devel/setup.bash" >> ~/.bashrc' \
 && echo 'export PS1="\[$(tput setaf 2; tput bold)\]\u\[$(tput setaf 7)\]@\[$(tput setaf 3)\]\h\[$(tput setaf 7)\]:\[$(tput setaf 4)\]\W\[$(tput setaf 7)\]$ \[$(tput sgr0)\]"' >> ~/.bashrc

RUN cd ~/ws \
 && catkin config --extend /opt/ros/noetic \
 && catkin build --no-status -DCMAKE_BUILD_TYPE=Release

