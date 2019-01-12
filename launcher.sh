#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Documents/smartbin3-master
sudo python3 photo.py
cd /

