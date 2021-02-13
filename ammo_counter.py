from machine import Pin
from digit import Digit
from button import Button
import time
import math
   
digit1 = Digit([0,0,0,0,0,0,0,0])
digit2 = Digit([0,0,0,0,0,0,0,0])

trigger_button = Button(0, Pin.IN, Pin.PULL_DOWN, 0)
magazine_button = Button(0, Pin.IN, Pin.PULL_DOWN, 0)

button_bounce_threshold = 0
 
ammo_capacity_on_reset = 0
current_ammo = 0
      
def initialise(digit1_pins, digit2_pins, trigger_button_pin, magazine_button_pin, bounce_threshold, maxmimum_ammo_capacity):
    global digit1
    global digit2    
    global trigger_button
    global magazine_button
    global button_bounce_threshold
    global ammo_capacity_on_reset
    
    digit1 = Digit(digit1_pins)
    digit2 = Digit(digit2_pins)
    
    button_bounce_threshold = bounce_threshold
    trigger_button = Button(trigger_button_pin, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)
    magazine_button = Button(magazine_button_pin, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)
    
    ammo_capacity_on_reset = maxmimum_ammo_capacity
    
    clear_ammo()
             
    while True:
        magazine_button_check()  
        trigger_button_check()    
        time.sleep(0.001)
        
def display_number(number):
    first_digit = math.floor(number / 10)
    second_digit = number % 10
    
    digit1.set_digit(first_digit)
    digit2.set_digit(second_digit)    
    
def set_ammo(number):
    global current_ammo
    current_ammo = number
    display_number(current_ammo)  
    
def decrease_ammo():
    if current_ammo > 0:
        set_ammo(current_ammo - 1)

def reset_ammo():
    set_ammo(ammo_capacity_on_reset)
    
def clear_ammo():
    set_ammo(0)
     
def magazine_button_check():
    magazine_button.update_button_state()
    if magazine_button.button_just_pressed():
        reset_ammo()
    if magazine_button.button_just_released():
        clear_ammo()
            
def trigger_button_check():
    trigger_button.update_button_state()        
    if trigger_button.button_just_pressed():
        decrease_ammo()