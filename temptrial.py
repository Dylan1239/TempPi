#!/usr/bin/python
import Adafruit_DHT
import socket

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO4.
pin = 4
retriesBeforeError = 3
#UDP_PORT = 8125
#UDP_IP = '138.68.192.105'


def getTempAndHumidityData(retryCount):
    if retryCount > retriesBeforeError:
        return None, None, 'Failed to get reading after' + `retriesBeforeError`

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   # temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        #appears to happen from time to time, get a wild reading where the humidity is over 100%
        if humidity > 100:
            return getTempAndHumidityData(retryCount + 1)


        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
        return humidity, temperature, None
    else:
        return getTempAndHumidityData(retryCount + 1)

#def reportGauge(gaugeName,gaugeValue):
   # message = gaugeName + ':' + `gaugeValue` + '|g'
   # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   #sock.sendto(message,(UDP_IP, UDP_PORT))

def main():
    humidity, temperature, error  = getTempAndHumidityData(0)
   # reportGauge('sensor1.humidity',humidity)
   # reportGauge('sensor1.temperature',temperature)

main()

