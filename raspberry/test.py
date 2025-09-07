from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from time import sleep

# Configuração da matriz 24x24 (3x3 módulos 8x8)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=24, height=24, rotate=0)

# Função para acender um LED específico
def set_led(x, y, value=True):
    device.pixel(x, y, value)
    device.show()

# Teste: acende LEDs um por um na matriz 24x24
for x in range(24):
    for y in range(24):
        set_led(x, y)
        sleep(0.05)  # espera 50ms antes do próximo LED
