#!/bin/bash

echo "configuring modules for tft fb"
echo "fbtft_device" >> /etc/modules-load.d/modules.conf
echo "options fbtft_device custom name=adafruit18 gpios=reset:1,dc:0,led:3 width=128 height=128 busnum=1" > /etc/modprobe.d/fbtft.conf

echo "installing required packages"
apt-get install python-pygame python-netifaces build-essential libi2c-dev i2c-tools python-dev libffi-dev -y
pip install smbus-cffi==0.5.1

echo "configuring autostart"
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
sed -e s/exit\ 0//g -i /etc/rc.local
sed -e s/will\ \"\"\ on\ success/will\ \"\exit\ 0\"\ on\ success/g -i /etc/rc.local
echo "python $SCRIPTPATH/main.py" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local
