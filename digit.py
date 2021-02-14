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
    
    def __init__(self, segment_pin_map, pwm_frequency):
        self.pin_map = [
            PWM(Pin(segment_pin_map[0])),
            PWM(Pin(segment_pin_map[1])),
            PWM(Pin(segment_pin_map[2])),
            PWM(Pin(segment_pin_map[3])),
            PWM(Pin(segment_pin_map[4])),
            PWM(Pin(segment_pin_map[5])),
            PWM(Pin(segment_pin_map[6])),
            PWM(Pin(segment_pin_map[7]))]
        
        for pwm in self.pin_map:
            pwm.freq(pwm_frequency)
                
    def set_digit(self, number, brightness = 0):
        segment_map = self.number_map[number]
        
        for i in range(0, len(segment_map)):
            self.pin_map[i].duty_u16((int)(65024 * (1 - (brightness * ( 1 - segment_map[i])))))
