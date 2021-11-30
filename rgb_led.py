# !/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Nov 2021
# This will display the LED over an interval of 1 second
#  and increase by 1 second more every on and off cycle 

import time
import board
import digitalio


# external LED is connected to pin 13 on the Pico
led_r = digitalio.DigitalInOut(board.GP13)
led_r.direction = digitalio.Direction.OUTPUT

led_g = digitalio.DigitalInOut(board.GP12)
led_g.direction = digitalio.Direction.OUTPUT

led_b = digitalio.DigitalInOut(board.GP11)
led_b.direction = digitalio.Direction.OUTPUT

while True: 
    led_r.value = True
    time.sleep(1.0)  
    led_g.value = True
    time.sleep(1.0)        
    led_b.value = True    
    time.sleep(1.0)
    led_r.value = True
    led_g.value = True
    time.sleep(1.0)
    led_g.value = True
    led_b.value = True
    time.sleep(1.0)
    led_b.value = True
    led_r.value = True
    time.sleep(1.0)
    led_r.value = True
    led_g.value = True
    led_b.value = True
    time.sleep(1.0)
