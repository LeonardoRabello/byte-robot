import os
from PIL import Image
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas

class Matrizes:
    def __init__(self, din=10, clk=11, cs=8, modulos_n=16):
        self.modulos_n = modulos_n
        self.default_image = "../faces/happy.png"

        self.serial = spi(port=0, device=0, gpio=noop())

        self.device = max7219(
            self.serial,
            cascaded=self.modulos_n,
            block_orientation=0,
            rotate=0
        )

    def mostrar_imagem(self, path):
        caminho = path if os.path.exists(path) else self.default_image
        img = Image.open(caminho).convert("1")

        self.device.clear()
        with canvas(self.device) as draw:
            draw.bitmap((0, 0), img, fill="white")

