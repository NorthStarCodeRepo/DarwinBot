# This version uses the new Adafruit library. The old Adafruit DHT library is deprecated.
# https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
# After fresh RPi OS install run the following
# sudo pip3 install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2
# Next: https://www.w3schools.com/python/ref_requests_post.asp
import adafruit_dht
import time
import board

# Board position #8, fourth down from top right
DHT_PIN = board.D14
dhtSensor = adafruit_dht.DHT11(DHT_PIN)
SLEEP_DURATION = 60
RETRY_DURATION = 5

# Slight startup delay to prevent sensor errors
print("Starting application...")
time.sleep(5)

while True:
    try:
        temp_c = dhtSensor.temperature
        humidity = dhtSensor.humidity
        if humidity is not None and temp_c is not None:
            # Convert to F
            print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(round((temp_c * 1.8) + 32), humidity))
        else:
            # If it fails then just set a retry pause and do it again
            time.sleep(RETRY_DURATION)
    except:
        # If it fails then just set a retry pause and do it again
        time.sleep(RETRY_DURATION)
    finally:
        time.sleep(SLEEP_DURATION)
