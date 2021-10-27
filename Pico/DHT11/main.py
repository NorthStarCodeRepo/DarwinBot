# Make it go blinky blink with a humidity sensor
# Connect using VBUS (5V) power, top right most pin
from machine import Pin, I2C
import utime as time
from DHT11 import DHT11, InvalidChecksum

max_humidity_for_warning = 55.0
is_warning = 0

onboard_light_pin = 16 # GPIO15
humidity_warning_light = machine.Pin(onboard_light_pin, machine.Pin.OUT)

# Delay any calls to the sensor until everything is loaded
# to pass the unstable status on boot up (ref. associated pdf)
time.sleep(5)

pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

# Turn the onboard LED on so we know the device is running
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(1)

while True:
	if is_warning == 1:
		for i in range(50):
			humidity_warning_light.toggle()
			time.sleep_ms(100)
	else:
		humidity_warning_light.value(0)

	time.sleep(5)
	print("Temperature: {}".format(sensor.temperature))
	print("Humidity: {}".format(sensor.humidity))
	
	if sensor.humidity >= max_humidity_for_warning:
		is_warning = 1
	else:
		is_warning = 0
