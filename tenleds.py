import RPi.GPIO as GPIO
from time import sleep

from config import PRINT_TO_CONSOLE

##############################
##############################
#####                    #####
#####     LED Pins       #####
#####                    #####
##############################
##############################

RED = 26
ORANGE = 13
YELLOW = 6
GREEN = 5
BLUE = 16
WHITE = 12
PINK = 25
PURPLE = 24
CHARTREUSE = 23
SOFTWHITE = 22

LED_ARRAY = [RED, ORANGE, YELLOW, GREEN, BLUE, WHITE, PINK, PURPLE, CHARTREUSE, SOFTWHITE]


##############################
##############################
#####                    #####
#####     Utilities      #####
#####                    #####
##############################
##############################

def set_up_pins():
    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)

    for x in LED_ARRAY:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.LOW)

def console(message):
    if PRINT_TO_CONSOLE:
        print(message)


def cleanup():
    console("Cleaning up GPIO...")
    GPIO.cleanup()
    console("Done")


##############################
##############################
#####                    #####
#####   Light Patterns   #####
#####                    #####
##############################
##############################


def starting_sequence():
    for x in LED_ARRAY:
            GPIO.output(x, GPIO.HIGH)
            sleep(0.3)
    
    sleep(1)
    
    for x in LED_ARRAY:
            GPIO.output(x, GPIO.LOW)


def marching(num=1, tim=0.05):
    for y in range(num):
        for x in LED_ARRAY:
            GPIO.output(x, GPIO.HIGH)
            sleep(tim)
            GPIO.output(x, GPIO.LOW)


def blink(num=1, tim=1):
    for y in range(num):
        for x in LED_ARRAY:
            GPIO.output(x, GPIO.HIGH)
        
        sleep(tim)

        for x in LED_ARRAY:
            GPIO.output(x, GPIO.LOW)

        sleep(tim)


def bounce(num=1, tim=0.05):
    for loop in range(num):
        z = 8

        for x in range(10):
            GPIO.output(LED_ARRAY[x], GPIO.HIGH)
            sleep(tim)
            GPIO.output(LED_ARRAY[x], GPIO.LOW)

        for y in range(8):
            GPIO.output(LED_ARRAY[z], GPIO.HIGH)
            sleep(tim)
            GPIO.output(LED_ARRAY[z], GPIO.LOW)
            z = z - 1


def cross(num=1, tim=0.05):
    for loop in range(num):
        x2 = 9

        for x in range(int(len(LED_ARRAY))):
            GPIO.output(LED_ARRAY[x], GPIO.HIGH)
            GPIO.output(LED_ARRAY[x2], GPIO.HIGH)
            sleep(tim)
            GPIO.output(LED_ARRAY[x], GPIO.LOW)
            GPIO.output(LED_ARRAY[x2], GPIO.LOW)
            x2 = x2 - 1


def two_marching(num=1, tim=0.2):
    for y in range(num):
        for x in range(10):

            if x > 7:
                new_x = x - 9
            else:
                new_x = x + 1
            
            GPIO.output(LED_ARRAY[x], GPIO.HIGH)
            GPIO.output(LED_ARRAY[new_x], GPIO.HIGH)
            sleep(tim)
            GPIO.output(LED_ARRAY[x], GPIO.LOW)
            GPIO.output(LED_ARRAY[new_x], GPIO.LOW)


def solid_on(tim=2):
    for x in LED_ARRAY:
        GPIO.output(x, GPIO.HIGH)
    
    sleep(tim)

    for x in LED_ARRAY:
        GPIO.output(x, GPIO.LOW)


##############################
##############################
#####                    #####
#####   Main Function    #####
#####                    #####
##############################
##############################


if __name__ == "__main__":
    
    try:
        set_up_pins()

        starting_sequence()

        while True:
            marching(10)
            bounce(5)
            two_marching(5, 0.1)
            cross(10)
            blink(3, 0.3)
            solid_on(1)

            # marching(1, 1)
            # bounce(1, 1)
            # two_marching(1, 1)
            # cross(1, 1)
            # blink(1, 1)
            # solid_on(1)

    except KeyboardInterrupt:
        console("CTRL-C was pressed...")
        blink(3, 0.1)
        console("Program terminated.")

    except Exception as e:
        console("Program stopped unexpectedly.")
        console(e)

    finally:
        cleanup()
        exit()