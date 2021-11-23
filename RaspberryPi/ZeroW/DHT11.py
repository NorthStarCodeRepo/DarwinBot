# https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
# sudo pip3 install Adafruit_DHT
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(round((temperature * 1.8) + 32), humidity))
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(5)
