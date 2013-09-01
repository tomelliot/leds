#import smbus
from leds import led

busNb = 1
address = 0x09
#bus = smbus.SMBus(1)
led1 = led(busNb, address)
led1.setrgb(0xFF, 0x00, 0x00)
led1.playscript(11, 0x00, 0x00)
