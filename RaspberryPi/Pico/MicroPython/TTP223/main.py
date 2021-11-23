# Turn a light on by touching a TTP223 touch sensor
# Connect using 3V3 power
import machine

touch = machine.Pin(15, machine.Pin.IN) # touch sensor input
led = machine.Pin(16, machine.Pin.OUT) # led light output
 
while True:
    led.value(touch.value()) # if it's 1 then turn the light on
