from machine import Pin
from digit import Digit
from button import Button
import time
import math
    
digit1 = Digit(7,6,5,4,3,2,1,0)
digit2 = Digit(8,9,10,11,12,13,14,15)

button_bounce_threshold = 20 #ms button has to be held down beforce input change registered

trigger_button = Button(18, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)
magazine_button = Button(17, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)

ammo_capacity = 10
current_ammo = 0

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
    set_ammo(ammo_capacity)
    
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
            
def initialise():
    clear_ammo()
             
    while True:
        magazine_button_check()  
        trigger_button_check()    
        time.sleep(0.001)