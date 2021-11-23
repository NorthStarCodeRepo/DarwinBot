# A very basic code to make a buzzing sound on a pizo buzzer
from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))

buzzer.freq(500)
buzzer.duty_u16(1000)
sleep(5)
buzzer.duty_u16(0)

buzzer.freq(1000)
buzzer.duty_u16(1000)
sleep(5)
buzzer.duty_u16(0)


buzzer.freq(800)
buzzer.duty_u16(1000)
sleep(5)
buzzer.duty_u16(0)
