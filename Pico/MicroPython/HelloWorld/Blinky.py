# Make it go blinky blink
import machine
import utime

onboard_led_pin_id = 25
light_on = 1
light_off = 0

led_onboard = machine.Pin(onboard_led_pin_id, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(0.5)
