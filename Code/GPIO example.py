import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode( GPIO.BCM ) # set board mode to Broadcom

GPIO.setup( 17, GPIO.IN, pull_up_down = GGPIO.PUD_DOWN ) # set up pin 17
GPIO.setup( 18, GPIO.OUT ) # set up pin 18

try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(17): # if port 17 == 1  
            print "Port 17 is 1/HIGH/True - LED ON"  
            GPIO.output(18, 1)         # set port/pin value to 1/HIGH/True  
        else:  
            print "Port 17 is 0/LOW/False - LED OFF"  
            GPIO.output(18, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
