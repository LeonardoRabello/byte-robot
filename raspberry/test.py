from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep

# Configuração da matriz 24x24 (3x3 módulos 8x8)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=24, height=24, rotate=0)

# Acende LEDs um por um
for x in range(24):
    for y in range(24):
        with canvas(device) as draw:
            draw.point((x, y), fill="white")
        sleep(0.05)
