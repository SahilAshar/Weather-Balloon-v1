#!/usr/bin/env bash 
# sensor_script.sh runs three python3 programs simultaneously
# this is primarily used to activate the sensors on board.


/usr/bin/python3 /home/pi/Documents/WBv1/Weather-Balloon-v1/src/BME280.py &
/usr/bin/python3 /home/pi/Documents/WBv1/Weather-Balloon-v1/src/BNO055.py &
/usr/bin/python3 /home/pi/Documents/WBv1/Weather-Balloon-v1/src/GPS.py &

 
