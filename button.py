from machine import Pin

class Button:
    
    button = Pin(0)
    button_bounce_threshold = 0
    button_bounce_value = 0
    previous_button_value = 0
    current_button_value = 0
    
    def __init__(self, pin, mode, pull, bounce_threshold):
        self.button = Pin(pin, mode, pull)
        self.button_bounce_threshold = bounce_threshold
    
    def button_just_pressed(self):
        return self.previous_button_value == 0 and self.current_button_value == 1
        
    def button_pressed(self):
        return self.current_button_value == 1
        
    def button_released(self):
        return self.current_button_value == 0
        
    def button_just_released(self):
        return self.previous_button_value == 1 and self.current_button_value == 0
    
    def update_button_state(self):
        if self.button_bounce_value < self.button_bounce_threshold:
            if self.button.value() != self.current_button_value:
                self.button_bounce_value += 1
            else:
                self.button_bounce_value = 0
        else:
            self.previous_button_value = self.current_button_value
            self.current_button_value = self.button.value()
        
            