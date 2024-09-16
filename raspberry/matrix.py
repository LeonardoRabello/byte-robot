from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import Image

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=16, height=8, block_orientation=90, rotate=0)

def desenhar():
    with canvas(device) as draw:
        draw.point((1, 1), fill="white")
        draw.point((6, 1), fill="white")
        draw.point((3, 5), fill="white")
        draw.point((4, 5), fill="white")
        draw.point((5, 5), fill="white")
        draw.arc((2, 2, 6, 6), start=45, end=135, fill="white")

desenhar()
        
        