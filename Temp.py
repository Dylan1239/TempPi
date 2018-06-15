#!/usr/bin/python
import sys
import Adafruit_DHT
gpio=13
sensor = Adafruit_DHT.DHT11


while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)



    print(humidity, temperature)
