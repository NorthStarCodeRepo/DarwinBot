# Use the PIR (Passive Infrared) SR501 sensor to turn on a light
# Use the VBUS (5V) very top right pin to power
import machine
import utime

sensor_pir = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_out = machine.Pin(16, machine.Pin.OUT)

def pir_handler(pin):
	utime.sleep_ms(100)
	if pin.value():
		print("Alarm! Motion Detected")
		for i in range(50):
			led_out.toggle()
			utime.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)