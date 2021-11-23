# Use the PIR (Passive Infrared) SR501 sensor to turn on a light
# Use the VBUS (5V) very top right pin to power
import machine
import utime

motion_detector_in = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_out = machine.Pin(16, machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(17))

def pir_handler(pin):
	utime.sleep_ms(100)
	if pin.value():
		print("Alarm! Motion Detected")
		for i in range(50):
			# toggle the led
			led_out.toggle()
			utime.sleep_ms(100)

			# toggle the buzzer
			buzzer.freq(1000)
			buzzer.duty_u16(1000)
		buzzer.duty_u16(0)

motion_detector_in.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)