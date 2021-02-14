import ammo_counter

digit1_pins = [7,6,5,4,3,2,1,0]       # a,b,c,d,e,f,g and dec. point pins for 7 segement display
digit2_pins = [8,9,10,11,12,13,14,15] # a,b,c,d,e,f,g and dec. point pins for 7 segement display

pwm_frequency = 100                  # Pulse Width Modulation frequency

trigger_button_pin = 18               # pin for button attached to the trigger
magazine_button_pin = 17              # pin for button attached to the magazine

button_bounce_threshold = 20          # ms button has to be held down beforce input change registered

ammo_capacity = 10                    # value that the counter will go to when magazine is inserted

time_to_low_power = 5                 # time in mins till low power mode is activate
low_power_brightness = 0.1            # brightness of digits in low power mode

time_to_super_low_power = 15          # time in mins till low power mode is activate
super_low_power_brightness = 0        # brightness of digits in low power mode

ammo_counter.initialise(digit1_pins, digit2_pins, pwm_frequency,
                        trigger_button_pin, magazine_button_pin, button_bounce_threshold,
                        time_to_low_power, low_power_brightness,
                        time_to_super_low_power, super_low_power_brightness,
                        ammo_capacity)
