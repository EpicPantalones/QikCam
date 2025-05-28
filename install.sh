#!/bin/bash
set -xe

sudo apt update
sudo apt upgrade -y
sudo apt install -y git zsh libcamera-dev libjpeg-dev python3-yaml

sudo dphys-swapfile swapoff
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile
sudo dphys-swapfile setup
sudo dphys-swapfile swapon

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

chsh -s /usr/bin/zsh

git clone https://github.com/EpicPantalones/QikCam.git