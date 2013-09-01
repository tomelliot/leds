import SMBus from smbus

class LEDS:
	def __init__(self, bus, address):
		self.bus = SMBus(bus)
		self.address = address

	
