# Make it go blinky blink
from machine import Pin, I2C
import utime as time
from DHT11 import DHT11, InvalidChecksum

onboard_led_pin_id = 25 # Pin GPIO25
max_humidity_for_warning = 55.0
is_warning = 0
onboard_light_pin = 15 # GPIO15
humidity_warning_light = machine.Pin(onboard_light_pin, machine.Pin.OUT)
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

led_onboard = machine.Pin(onboard_led_pin_id, machine.Pin.OUT)

# Turn the onboard LED on so we know the device is running
led_onboard.value(1)

def ControlLight(light_state):
	if light_state == 1:
		while True:
			humidity_warning_light.value(1)
			time.sleep(0.1)
			humidity_warning_light.value(0)
			time.sleep(0.1)
			humidity_warning_light.value(1)
			time.sleep(0.1)
			humidity_warning_light.value(0)
			time.sleep(0.1)
			humidity_warning_light.value(1)
			time.sleep(0.1)
			humidity_warning_light.value(0)
			time.sleep(0.1)
			humidity_warning_light.value(1)
			time.sleep(0.1)
			humidity_warning_light.value(0)
			time.sleep(0.1)
			break
	else:
		humidity_warning_light.value(0)

while True:
	if is_warning == 1:
		ControlLight(1)
	else:
		ControlLight(0)

	time.sleep(5)
	print("Temperature: {}".format(sensor.temperature))
	print("Humidity: {}".format(sensor.humidity))
	
	if sensor.humidity > max_humidity_for_warning:
		is_warning = 1
	else:
		is_warning = 0
