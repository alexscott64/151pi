import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
p=GPIO.PWM(2,207)
p.start(0)
try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            