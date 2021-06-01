import time

from board import SCL, SDA

import busio

from adafruit_seesaw.seesaw import Seesaw 

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
	touch = ss.moisture_read()
	temp = ss.get_temp()


	tempF = (temp * 9/5) + 32
	print("temp: " + str(tempF) + " moisture: " + str(touch))
	time.sleep(1)
