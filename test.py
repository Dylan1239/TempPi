import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(3, GPIO.OUT)
sensor = Adafruit_DHT.DHT11

while True:
	i=GPIO.input(13)
	humidity, temperature = Adafruit_DHT.read_retry(sensor, i)

	print (humidity, temperature)
