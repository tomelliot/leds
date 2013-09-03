from leds import led
from random import randint 


busNb = 1
address = 0x09
led1 = led(busNb, address)
led1.setrgb(randint(1, 255), randint(1, 255), randint(1, 255))
#print led1.getfirmware()
#print led1.getaddr()
#print led1.getrgb()
print led1.readscript(2, 3)
