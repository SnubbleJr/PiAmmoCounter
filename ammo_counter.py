from machine import Pin
from digit import Digit
from button import Button
import time
import math
   
digit1 = Digit([0,0,0,0,0,0,0,0],1000)
digit2 = Digit([0,0,0,0,0,0,0,0],1000)

trigger_button = Button(0, Pin.IN, Pin.PULL_DOWN, 0)
magazine_button = Button(0, Pin.IN, Pin.PULL_DOWN, 0)

button_bounce_threshold = 0
 
time_to_low_power = 0
low_power_brightness = 0

time_to_super_low_power = 0
super_low_power_brightness = 0

time_idle = 0
current_brightness = 1

ammo_capacity_on_reset = 0
current_ammo = 0
      
def initialise(digit1_pins, digit2_pins, pwm_frequency,
               trigger_button_pin, magazine_button_pin, bounce_threshold,
               time_to_lp, lp_brightness,
               time_to_slp, slp_brightness,
               maxmimum_ammo_capacity):
    global digit1
    global digit2
    
    global trigger_button
    global magazine_button
    global button_bounce_threshold
    
    global time_to_low_power
    global low_power_brightness
    
    global time_to_super_low_power
    global super_low_power_brightness
    
    global ammo_capacity_on_reset
    
    digit1 = Digit(digit1_pins, pwm_frequency)
    digit2 = Digit(digit2_pins, pwm_frequency)
    
    time_to_low_power = time_to_lp * 60000
    low_power_brightness = lp_brightness
    
    time_to_super_low_power = time_to_slp * 60000
    super_low_power_brightness = slp_brightness
    
    button_bounce_threshold = bounce_threshold
    trigger_button = Button(trigger_button_pin, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)
    magazine_button = Button(magazine_button_pin, Pin.IN, Pin.PULL_DOWN, button_bounce_threshold)
    
    ammo_capacity_on_reset = maxmimum_ammo_capacity

    clear_ammo()
             
    while True:
        magazine_button_check()  
        trigger_button_check()
        idle_check()
        time.sleep(0.001)
        
def idle_check():
    global time_idle
    global current_brightness
    
    time_idle += 1
    
    if time_idle >= time_to_low_power:
        if time_idle >= time_to_super_low_power:
            if current_brightness != super_low_power_brightness:
                current_brightness = super_low_power_brightness
                set_ammo(current_ammo)
        else:
            if current_brightness != low_power_brightness:
                current_brightness = low_power_brightness
                set_ammo(current_ammo)
        
def wake_up():
    global time_idle
    global current_brightness
    
    time_idle = 0
    current_brightness = 1
def display_number(number):
    first_digit = math.floor(number / 10)
    second_digit = number % 10
    
    digit1.set_digit(first_digit, current_brightness)
    digit2.set_digit(second_digit, current_brightness)    
    
def set_ammo(number):
    global current_ammo
    current_ammo = number
    display_number(current_ammo)  
    
def decrease_ammo():
    if current_ammo > 0:
        wake_up()
        set_ammo(current_ammo - 1)

def reset_ammo():
    wake_up()
    set_ammo(ammo_capacity_on_reset)
    
def clear_ammo():
    wake_up()
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