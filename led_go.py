#import smbus
import led

busNb = 1
address = 0x09
#bus = smbus.SMBus(1)
led.init(busNb, address)
led.setcolour(0x00, address, 0xFF, 0x00, 0x00)
