# Turn a light on with a motion sensor - MH Flying Fish
from machine import Pin
import utime

led = Pin(16, Pin.OUT)
pirsensor = Pin(15, Pin.IN, Pin.PULL_UP)
led.low()

utime.sleep(7)

while True:
    print(pirsensor.value())
    if pirsensor.value() == 0:
        print("LED On")
        led.high()
        utime.sleep(7)
    else:
        print("Waiting for movement")
        led.low()
	
	utime.sleep(0.7)
