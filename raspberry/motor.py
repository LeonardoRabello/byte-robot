import keyboard
import pigpio
from time import sleep


class Motor:
    def __init__(self, PWM1, PWM2, R_EN1, L_EN1, R_EN2, L_EN2):
        self.pi = pigpio.pi()


















































        
        self.freq = 1000  # Hz

        # Configura enable/direção como saída digital
        for pin in [R_EN1, L_EN1, R_EN2, L_EN2]:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.write(pin, 0)  # garante motor parado no início

    def move_foward(self, speed):
        self.pi.write(self.R_EN1, 1)
        self.pi.write(self.L_EN1, 0)
        self.pi.write(self.R_EN2, 1)
        self.pi.write(self.L_EN2, 0)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000))

    def move_back(self, speed):
        self.pi.write(self.R_EN1, 0)
        self.pi.write(self.L_EN1, 1)
        self.pi.write(self.R_EN2, 0)
        self.pi.write(self.L_EN2, 1)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000))

    def move_right(self, speed):
        self.pi.write(self.R_EN1, 1)
        self.pi.write(self.L_EN1, 0)
        self.pi.write(self.R_EN2, 1)
        self.pi.write(self.L_EN2, 0)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000 / 2))

    def move_left(self, speed):
        self.pi.write(self.R_EN1, 1)
        self.pi.write(self.L_EN1, 0)
        self.pi.write(self.R_EN2, 1)
        self.pi.write(self.L_EN2, 0)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000 / 2))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000))

    def move_back_left(self, speed):
        self.pi.write(self.R_EN1, 0)
        self.pi.write(self.L_EN1, 1)
        self.pi.write(self.R_EN2, 0)
        self.pi.write(self.L_EN2, 1)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000 / 2))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000))

    def move_back_right(self, speed):
        self.pi.write(self.R_EN1, 0)
        self.pi.write(self.L_EN1, 1)
        self.pi.write(self.R_EN2, 0)
        self.pi.write(self.L_EN2, 1)
        self.pi.hardware_PWM(self.PWM1, self.freq, int(speed * 10000))
        self.pi.hardware_PWM(self.PWM2, self.freq, int(speed * 10000 / 2))

    def breaks(self):
        self.pi.write(self.R_EN1, 0)
        self.pi.write(self.L_EN1, 0)
        self.pi.write(self.R_EN2, 0)
        self.pi.write(self.L_EN2, 0)
        self.pi.hardware_PWM(self.PWM1, 0, int(0))
        self.pi.hardware_PWM(self.PWM2, 0, int(0))

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
                break
            sleep(0.1)  # pequeno delay para evitar uso excessivo da CPU
        self.pi.stop()
