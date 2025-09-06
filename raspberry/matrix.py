from luma.led_matrix.device import max7219
from luma.emulator.device import pygame
from PIL import Image


class faces:
    def __init__(self, contrast: int = 127):
        self.matrix = pygame(24, 24, 0, "1")
        self.matrix.contrast(contrast)

    def split_face_and_message(self, message: str):
        output, face = message.split("| ")
        return output, face

    def show_face(self, file: str):
        try:
            face = Image.open(f"faces/{file}")
        except:
            face = "happy.png"
        self.matrix.display(face)


