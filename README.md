
## Raspberry Pi Connections
Use images provided in [this](https://medium.com/initial-state/how-to-use-a-soil-moisture-sensor-to-keep-your-plants-alive-51a2294b88e) link to connect wires to soil sensor and raspberry pi

## Prerequisites
Instructions retrieved from [here](https://medium.com/initial-state/how-to-use-a-soil-moisture-sensor-to-keep-your-plants-alive-51a2294b88e)
1. Bring up raspberry pi config menu: `sudo raspi-config`
2. Turn on peripherals (number 5 in selection menu, click enter)

3. Test to make sure you enabled: `sudo i2cdetect -y 1`

4. Install these libraries:
```
pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-seesaw
sudo pip3 install adafruit-circuitpython-bh1750 #for the light module - dont need if not using the light module
sudo pip3 install ISStreamer #I don't think this is needed - not using the described streaming they mentioned.  Instead, I wrote a really basic python server to serve requests
```
## Enable SSH

If you want to run this from elsewhere (eg running commands from your desktop computer on your raspberry pi), you likely want to enable ssh.  Here are the basic setup instructions

NOTE: YOU ARE GOING TO WANT TO SET A DIFFERENT PASSWORD THAN THE DEFAULT FOR YOUR RASPBERRY PI IF ENABLING SSH FOR SECURITY PURPOSES

See article [here](https://www.raspberrypi.org/documentation/remote-access/ssh/)

## Python code
TODO: See [this](https://koenwoortman.com/python-flask-return-json-response/) to make it better

## Client script
The client script `run-client.sh` specifies a simple curl command to use the raspberry pi server to serve requests. The script can take in the server ip and sleep time between commands or uses the defaults if they are not passed in 
