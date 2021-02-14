from machine import Pin, PWM

class Digit:
    
    number_map = {
        0: [
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1
            ],
        1: [
            1,
            0,
            0,
            1,
            1,
            1,
            1,
            1
            ],
        2: [
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            1
            ],
        3: [
            0,
            0,
            0,
            0,
            1,
            1,
            0,
            1
            ],
        4: [
            1,
            0,
            0,
            1,
            1,
            0,
            0,
            1
            ],
        5: [
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            1
            ],
        6: [
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            1
            ],
        7: [
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1
            ],
        8: [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1
            ],
        9: [
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            1
            ],
        ".": [            
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0
            ],
        "": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            ]
        }
    
    #order of pin map is:
    #pin_a
    #pin_b
    #pin_c
    #pin_d
    #pin_e
    #pin_f
    #pin_g
    #pin_dc
    
    pin_map = []
    
    def __init__(self, pin_map, pwm_frequency):
        for i in range(0, len(pin_map)):
            pwn = PWM(Pin(pin_map[i]))
            pwn.freq(pwm_frequency)
            self.pin_map.insert(0, pwn)
        
    def set_digit(self, number, brightness = 1):
        segment_map = self.number_map[number]
        
        for i in range(0, len(segment_map)):
            self.pin_map[i].duty_u16((int)(65025 * brightness))
