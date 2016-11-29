# University of North Texas, College of Engineering
# EENG 4910/4990 - Senior Design
#
# Fall 2016 & Spring 2017
#
# Students: Nathan Ruprecht
#           Chris Askings
#           Forrest Gates
#
# Mentor: Dr. Kamesh Namuduri
#
# Documentation Statement:  I got GPIO template code
# from Alex Eames who is with RasPi.TV.  Started with
# tutorials from 17 July 2013.
#
# Used ADC script from adafruit.  URL below:
# https://learn.adafruit.com/reading-a-analog-in-and
# -controlling-audio-volume-with-the-raspberry-pi/script
#

# Imports
import RPi.GPIO as GPIO
import time

# Choose .BCM or .BOARD
GPIO.setmode( GPIO.BCM )

# Constants
SCLK = 18
MISO = 23
MOSI = 24
CS = 25
MESSAGE_LENGTH = 32
SAMPLE_FREQ = 5000
PACKET = 0x00000000

# Set up Inputs
GPIO.setup( MISO, GPIO.IN )

# Set up Outputs
GPIO.setup( MOSI, GPIO.OUT )
GPIO.setup( SCLK, GPIO.OUT )
GPIO.setup( CS, GPIO.OUT )

def main():
    #Photodiode circuit connected to adc #0
    PhotoD = 0;

    while 1: #Infinite loop
        while( start_bit() ): #Wait for start bit pattern (0x9)
            receive_data() #Receive message
            analyze_data() #Decode and output message

def start_bit():
    #See the change between logic 1 and 0 from the ADC
    if( read_adc( PhotoD, CLK, MOSI, MISO, CS) ):
        pin = 1
    else:
        pin = 0

    if( pin ):#Rising edge
        #reset timer
        #start timer
    else:#Falling edge
        #stop timer
        elapsedTime = endTime - startTime
        f = 1 / elapsedTime
        #Shift the packet 1 bit to the left and
        #put the new bit from the ADC into the LSB
        if( f == (2*SAMPLE_FREQ) ):
            PACKET = ( PACKET << 1 ) | 1 #Logic 1
        if( f == SAMPLE_FREQ ):
            PACKET = ( PACKET << 1 ) | 0 #Logic 0

    
    if( PACKET == 0x9 ):
        return True
    else:
        return False

def receive_data():
    #See the change between logic 1 and 0 from the ADC
    if( read_adc( PhotoD, CLK, MOSI, MISO, CS) ):
        pin = 1
    else:
        pin = 0

    if( pin ):#Rising edge
        #reset timer
        #start timer
    else:#Falling edge
        #stop timer
        elapsedTime = endTime - startTime
        f = 1 / elapsedTime
        #Shift the packet 1 bit to the left and
        #put the new bit from the ADC into the LSB
        if( f == (2*SAMPLE_FREQ) ):
            PACKET = ( PACKET << 1 ) | 1 #Logic 1
        if( f == SAMPLE_FREQ ):
            PACKET = ( PACKET << 1 ) | 0 #Logic 0

def analyze_data():
    print( ascii_table( PACKET ) )
    
def read_adc( adcnum, clockpin, mosipin, misopin, cspin ):
    if ((adcnum > 7) or (adcnum < 0)):
            return -1
    GPIO.output(cspin, True)
 
    GPIO.output(clockpin, False)  #Start clock low
    GPIO.output(cspin, False)     #Bring CS low
 
    commandout = adcnum
    commandout |= 0x18  #Start bit + single-ended bit
    commandout <<= 3    #We only need to send 5 bits here
    for i in range(5):
            if (commandout & 0x80):
                    GPIO.output(mosipin, True)
            else:
                    GPIO.output(mosipin, False)
            commandout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
 
    adcout = 0
    #Read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
            adcout <<= 1
            if (GPIO.input(misopin)):
                    adcout |= 0x1
 
    GPIO.output(cspin, True)
       
    adcout >>= 1       #First bit is 'null' so drop it
    return adcout

def ascii_table(dataIn):
    if( dataIn == 0x20 ):
        return ' '
    elif( dataIn == 0x21 ):
        return '!'
    elif( dataIn == 0x22 ):
        return '"'
    elif( dataIn == 0x23 ):
        return '#'
    elif( dataIn == 0x24 ):
        return '$'
    elif( dataIn == 0x25 ):
        return '%'
    elif( dataIn == 0x26 ):
        return '&'
    elif( dataIn == 0x27 ):
        return "'"
    elif( dataIn == 0x28 ):
        return '('
    elif( dataIn == 0x29 ):
        return ')'
    elif( dataIn == 0x2A ):
        return '*'
    elif( dataIn == 0x2B ):
        return '+'
    elif( dataIn == 0x2C ):
        return ','
    elif( dataIn == 0x2D ):
        return '_'
    elif( dataIn == 0x2E ):
        return '.'
    elif( dataIn == 0x2F ):
        return '/'
    elif( dataIn == 0x30 ):
        return '0'
    elif( dataIn == 0x31 ):
        return '1'
    elif( dataIn == 0x32 ):
        return '2'
    elif( dataIn == 0x33 ):
        return '3'
    elif( dataIn == 0x34 ):
        return '4'
    elif( dataIn == 0x35 ):
        return '5'
    elif( dataIn == 0x36 ):
        return '6'
    elif( dataIn == 0x37 ):
        return '7'
    elif( dataIn == 0x38 ):
        return '8'
    elif( dataIn == 0x39 ):
        return '9'
    elif( dataIn == 0x3A ):
        return ':'
    elif( dataIn == 0x3B ):
        return ';'
    elif( dataIn == 0x3C ):
        return '<'
    elif( dataIn == 0x3D ):
        return '='
    elif( dataIn == 0x3E ):
        return '>'
    elif( dataIn == 0x3F ):
        return '?'
    elif( dataIn == 0x40 ):
        return '@'
    elif( dataIn == 0x41 ):
        return 'A'
    elif( dataIn == 0x42 ):
        return 'B'
    elif( dataIn == 0x43 ):
        return 'C'
    elif( dataIn == 0x44 ):
        return 'D'
    elif( dataIn == 0x45 ):
        return 'E'
    elif( dataIn == 0x46 ):
        return 'F'
    elif( dataIn == 0x47 ):
        return 'G'
    elif( dataIn == 0x48 ):
        return 'H'
    elif( dataIn == 0x49 ):
        return 'I'
    elif( dataIn == 0x4A ):
        return 'J'
    elif( dataIn == 0x4B ):
        return 'K'
    elif( dataIn == 0x4C ):
        return 'L'
    elif( dataIn == 0x4D ):
        return 'M'
    elif( dataIn == 0x4E ):
        return 'N'
    elif( dataIn == 0x4F ):
        return 'O'
    elif( dataIn == 0x50 ):
        return 'P'
    elif( dataIn == 0x51 ):
        return 'Q'
    elif( dataIn == 0x52 ):
        return 'R'
    elif( dataIn == 0x53 ):
        return 'S'
    elif( dataIn == 0x54 ):
        return 'T'
    elif( dataIn == 0x55 ):
        return 'U'
    elif( dataIn == 0x56 ):
        return 'V'
    elif( dataIn == 0x57 ):
        return 'W'
    elif( dataIn == 0x58 ):
        return 'X'
    elif( dataIn == 0x59 ):
        return 'Y'
    elif( dataIn == 0x5A ):
        return 'Z'

if __name__ == "__main__":
    main()
