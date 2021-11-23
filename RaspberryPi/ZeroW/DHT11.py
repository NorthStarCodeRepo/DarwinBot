# https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
# After fresh RPi OS install run the following
# sudo pip3 install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2
# Next: https://www.w3schools.com/python/ref_requests_post.asp
import adafruit_dht
import time
import board

DHT_PIN = board.D14 # Board position #8, fourth down from top right
dhtSensor = adafruit_dht.DHT11(DHT_PIN)

while True:
    try:
        temp_c = dhtSensor.temperature
        humidity = dhtSensor.humidity
        if humidity is not None and temp_c is not None:
            print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(round((temp_c * 1.8) + 32), humidity))
        else:
            print("Sensor failure. Check wiring.")
    except:
        print("Sensor failure. Check wiring.")
    finally:
        time.sleep(5)
