from machine import Pin

class Digit:
    
    number_map = {
        0: [
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            True
            ],
        1: [
            True,
            False,
            False,
            True,
            True,
            True,
            True,
            True
            ],
        2: [
            False,
            False,
            True,
            False,
            False,
            True,
            False,
            True
            ],
        3: [
            False,
            False,
            False,
            False,
            True,
            True,
            False,
            True
            ],
        4: [
            True,
            False,
            False,
            True,
            True,
            False,
            False,
            True
            ],
        5: [
            False,
            True,
            False,
            False,
            True,
            False,
            False,
            True
            ],
        6: [
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            True
            ],
        7: [
            False,
            False,
            False,
            True,
            True,
            True,
            True,
            True
            ],
        8: [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True
            ],
        9: [
            False,
            False,
            False,
            False,
            True,
            False,
            False,
            True
            ],
        ".": [            
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False
            ],
        "": [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
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
    
    def __init__(self, pin_map):
        self.pin_map = [
            Pin(pin_map[0], Pin.OUT),
            Pin(pin_map[1], Pin.OUT),
            Pin(pin_map[2], Pin.OUT),
            Pin(pin_map[3], Pin.OUT),
            Pin(pin_map[4], Pin.OUT),
            Pin(pin_map[5], Pin.OUT),
            Pin(pin_map[6], Pin.OUT),
            Pin(pin_map[7], Pin.OUT)
            ]
        
    def set_digit(self, number):
        segment_map = self.number_map[number]
        
        for i in range(0, len(segment_map)):
            self.pin_map[i].value(segment_map[i])
        
