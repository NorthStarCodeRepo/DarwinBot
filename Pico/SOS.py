# Sending out an SOS
import machine
import utime

onboard_led_pin_id = 25
light_on = 1
light_off = 0
dot_length = 0.20
dash_length = 0.60

led_onboard = machine.Pin(onboard_led_pin_id, machine.Pin.OUT)

def print_S():
	led_onboard.value(light_on)
	utime.sleep(dot_length)
	led_onboard.value(light_off)
	utime.sleep(dot_length)
	led_onboard.value(light_on)
	utime.sleep(dot_length)
	led_onboard.value(light_off)
	utime.sleep(dot_length)
	led_onboard.value(light_on)
	utime.sleep(dot_length)
	led_onboard.value(light_off)

def print_O():
	led_onboard.value(light_on)
	utime.sleep(dash_length)
	led_onboard.value(light_off)
	utime.sleep(dash_length)
	led_onboard.value(light_on)
	utime.sleep(dash_length)
	led_onboard.value(light_off)
	utime.sleep(dash_length)
	led_onboard.value(light_on)
	utime.sleep(dash_length)
	led_onboard.value(light_off)

while True:
	print_S()
	utime.sleep(1)
	print_O()
	utime.sleep(1)
	print_S()
	utime.sleep(2)
