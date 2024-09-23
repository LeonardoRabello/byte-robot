from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time
import json
print(1)
with open("../faces.json", 'r') as file:
    faces = json.load(file)
print(1)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=8, height=8, block_orientation=90, rotate=0)
def draw_bitmap(bitmap):
    with canvas(device) as draw:
        for y in range(8):
            for x in range(8):
                if bitmap[y] & (1<<(15-x)):
                    draw.point((x, y), fill='white')
print(1)
face_bitmap = [0b11100001,
               0b00000001,
               0b00000001,
               0b00000000,
               0b00000000,
               0b10000000,
               0b10000000,
               0b10000111]
print(1)
try:
    while True:
        print(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        draw_bitmap(face_bitmap)
        time.sleep(1)
except KeyboardInterrupt:
        pass
    


