#!/bin/bash
set -xe

echo "----------------- Upgrading System -----------------"
sudo apt update
sudo apt upgrade -y

echo "----------------- Installing Dependencies -----------------"
sudo apt install -y git libcamera-dev libjpeg-dev libtiff5-dev libboost-program-options-dev libdrm-dev libexif-dev

echo "------------------- Setting up Swapfile -------------------"
sudo dphys-swapfile swapoff
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile
sudo dphys-swapfile setup
sudo dphys-swapfile swapon

git clone https://github.com/EpicPantalones/QikCam.git
cd QikCam
python3 -m pip install yaml