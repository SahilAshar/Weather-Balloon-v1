#the IMU
import datetime
import time
import board
import busio
import adafruit_bno055

f = open("bno055.txt", "a+") #appends a file, creates new one if not there, can create file in the initilization by f = open("bme280.txt", "w+")
f.write("Time    Temperature    Accelerometer    Magnetometer    Gyroscope    Euler angle     Quaternion    Linear acceleration    Gravity\n")

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)


while True:
    f.write(str(datetime.datetime.now()) )
    f.write('    {}    '.format(sensor.temperature))
    f.write('{}    ' .format(sensor.accelerometer))
    f.write('{}    '.format(sensor.magnetometer))
    f.write('{}    '.format(sensor.gyroscope))
    f.write('{}    '.format(sensor.euler))
    f.write('{}    '.format(sensor.quaternion))
    f.write('{}    '.format(sensor.linear_acceleration))
    f.write('{}\n'.format(sensor.gravity))
    time.sleep(1) #however long we want, in seconds

