# Connect the data cable to D0, leave A0 empty for resistive type (has a small probe in between)
# This sensor returns either 1 for no moisture present or 0 for moisture present
# Use the screw on the intermediate probe to adjust moisture sensitivity
import machine
import utime

onboard_led = machine.Pin(25, machine.Pin.OUT)
data_in = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
	utime.sleep(2)
	is_moisture = data_in.value()
	if is_moisture == 1: # no moisture present, light on needs water
		print(data_in.value())
		onboard_led.value(1)
	else:
		print(data_in.value())
		onboard_led.value(0)