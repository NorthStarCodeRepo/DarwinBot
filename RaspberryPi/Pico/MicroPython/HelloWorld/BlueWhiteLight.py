# Make it go blinky blink
import machine
import utime

blue_light = 15
white_light = 16
onboard_led_pin_id = 25

light_on = 1
light_off = 0

led_onboard = machine.Pin(onboard_led_pin_id, machine.Pin.OUT)
blue_light_onboard = machine.Pin(blue_light, machine.Pin.OUT)
white_light_onboard = machine.Pin(white_light, machine.Pin.OUT)

# Turn the onboard LED on so we know the device is running
led_onboard.value()

while True:
    blue_light_onboard.value(light_on)
    utime.sleep(0.5)
    blue_light_onboard.value(light_off)
    utime.sleep(0.5)
    white_light_onboard.value(light_on)
    utime.sleep(0.5)
    white_light_onboard.value(light_off)
    utime.sleep(0.5)