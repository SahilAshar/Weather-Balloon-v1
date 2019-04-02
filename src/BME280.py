# TODO: @Dylan
#
# Set-Up BME280.py
# Don't worry about library downloads
# Instead of printing data like the GitHub repo shows,
# need to be stored in a text file called bme280.txt
#
# Look up how to do that in Python
# Look over all documentation for all sensors(in GitHub repo)

#let use this to create text file in initilization


import datetime
import time
import board
import busio
import adafruit_bme280

f = open("/home/pi/Documents/WBv1/Weather-Balloon-v1/output/bme280.txt", "a+") #appends a file, creates new one if not there, can create file in the initilization by f = open("bme280.txt", "w+")
f.write("Time    Tempurature    Humidity    Pressure    Altitude\n")

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
	f.write(str(datetime.datetime.now()) )
	f.write("    %0.1f" % bme280.temperature)
	f.write("    %0.1f" % bme280.humidity)
	f.write("    %0.1f" % bme280.pressure)
	f.write("    %0.2f\n" % bme280.altitude)
	f.flush()
	time.sleep(2) #however long we want, in seconds

f.close()
