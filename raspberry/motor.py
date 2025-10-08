
import RPi.GPIO as GPIO
import keyboard

class Motor():
    def __init__(self, RPWM1, LPWM1, RPWM2, LPWM2):
        GPIO.setup(RPWM1, GPIO.OUT)
        GPIO.setup(LPWM1, GPIO.OUT)
        GPIO.setup(RPWM2, GPIO.OUT)
        GPIO.setup(LPWM2, GPIO.OUT)
        self.foward_speed_1 = GPIO.PWM(RPWM1, 1000)
        self.reverse_speed_1 = GPIO.PWM(LPWM1, 1000)
        self.foward_speed_2 = GPIO.PWM(RPWM2, 1000)
        self.reverse_speed_2 = GPIO.PWM(LPWM2, 1000)

    def move_foward(self, speed):
        self.foward_speed_1.start(speed)
        self.foward_speed_2.start(speed)
        self.reverse_speed_1.start(0)
        self.reverse_speed_2.start(0)
    def move_back(self, speed):
        self.foward_speed_1.start(0)
        self.foward_speed_2.start(0)
        self.reverse_speed_1.start(speed)
        self.reverse_speed_2.start(speed)
    def move_right(self, speed):
        self.foward_speed_1.start(speed)
        self.foward_speed_2.start(speed / 2)
        self.reverse_speed_1.start(0)
        self.reverse_speed_2.start(0)
    def move_left(self, speed):
        self.foward_speed_1.start(speed / 2)
        self.foward_speed_2.start(speed)
        self.reverse_speed_1.start(0)
        self.reverse_speed_2.start(0)
    def move_back_left(self, speed):
        self.foward_speed_1.start(0)
        self.foward_speed_2.start(0)
        self.reverse_speed_1.start(speed / 2)
        self.reverse_speed_2.start(speed)
    def move_back_right(self, speed):
        self.foward_speed_1.start(0)
        self.foward_speed_2.start(0)
        self.reverse_speed_1.start(speed)
        self.reverse_speed_2.start(speed / 2)
    def breaks(self):
        self.foward_speed_1.start(0)
        self.foward_speed_2.start(0)
        self.reverse_speed_1.start(0)
        self.reverse_speed_2.start(0)
    def move(self, speed):
        while True:
            if keyboard.is_pressed('W'):
                self.move_foward(speed)
            elif keyboard.is_pressed('S'):
                self.move_back(speed)
            elif keyboard.is_pressed('Q'):
                self.move_left(speed)
            elif keyboard.is_pressed('E'):
                self.move_right(speed)
            elif keyboard.is_pressed('A'):
                self.move_back_left(speed)
            elif keyboard.is_pressed('D'):
                self.move_back_right(speed)
            elif keyboard.is_pressed('X'):
                breakpoint
            else:
                self.breaks()



    
