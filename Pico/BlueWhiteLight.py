# Make it go blinky blink
import machine
import utime

onboard_led_pin_id = 25
blue_light = 15
white_light = 16
light_on = 1
light_off = 0

led_onboard = machine.Pin(onboard_led_pin_id, machine.Pin.OUT)
blue_light_onboard = machine.Pin(blue_light, machine.Pin.OUT)
white_light_onboard = machine.Pin(white_light, machine.Pin.OUT)

# while True:
#     led_onboard.toggle()
#     utime.sleep(0.5)

led_onboard.toggle()
blue_light_onboard.toggle()
white_light_onboard.toggle()