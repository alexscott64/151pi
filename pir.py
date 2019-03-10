# motion sensor
import time
import RPi.GPIO as GPIO

#from gpiozero import MotionSensor

#pir = MotionSensor(4)

#while True:
    #pir.wait_for_motion()
    #print("You moved")
    #pir.wait_for_no_motion()

sensor=11
motor=7


GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)
cs=0
try:
    while True:
        time.sleep(0.1)
        cs=GPIO.input(sensor)
        if cs==1:
            print('GPIO pin %s is %s' % (sensor,cs))
            GPIO.output(motor,True)
            time.sleep(1)
            GPIO.output(motor,False)
            time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
