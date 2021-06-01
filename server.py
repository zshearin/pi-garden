import time

from board import SCL, SDA
from flask import Flask, jsonify

import busio

from adafruit_seesaw.seesaw import Seesaw 

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

api = Flask(__name__)

@api.route('/sensor', methods=['GET'])
def get_sensor_values():
	touch = ss.moisture_read()
	tempC = ss.get_temp()
	tempF = (tempC * 9/5) + 32
	sensors = {"moisture": touch, "temperature": tempF}
	#return json.dumps(sensors)
	return jsonify(sensors)
	#tempF = (temp * 9/5) + 32
	#print("temp: " + str(tempF) + " moisture: " + str(touch))
	#time.sleep(1)

if __name__ == '__main__':
	api.run(host='0.0.0.0', port=8090)
