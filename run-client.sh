#!/bin/bash

#IP Address of raspberry pi.  If not specified on input, uses latter value
RPI_IP=$([ "$2" != "" ] && echo "$2" || echo "192.168.1.156")

#Sleep time between requests (in seconds).  If not specified, uses default value of 5
SLEEP_TIME=$([ "$1" != "" ] && echo "$1" || echo "5")

#echo $a 
while : ; do curl -X GET http://${RPI_IP}:8090/sensor && sleep ${SLEEP_TIME}; done

