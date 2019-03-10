import RPi.GPIO as GPIO
import time 
from time import sleep

GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23

PIN_TRIGGER = 7
PIN_ECHO = 11

 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)



def moveForward():
	print("Go forward")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	sleep(3)
           
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)


def moveBack():
	print("Go back")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	sleep(3)
           
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)












print( "Waiting for sensor to settle")

try:
	distance = 9999999
	while( distance >= 20 ):
		sleep(1)
       		print("Calculating Distance")
		GPIO.output(PIN_TRIGGER, GPIO.HIGH)
		sleep(0.00001)
	
		GPIO.output(PIN_TRIGGER, GPIO.LOW)

		while GPIO.input(PIN_ECHO)==0:
            		pulse_start_time = time.time()
      		while GPIO.input(PIN_ECHO)==1:
            		pulse_end_time = time.time()

        	pulse_duration = pulse_end_time - pulse_start_time
        	distance = round(pulse_duration * 17150, 2)
        	print( "Distance:",distance,"cm" )


	print("moving forward now")
	moveForward()
	sleep(20)
	moveBack()

        print("End of cycle")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

