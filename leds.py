# implements commands for BlinkM module
# Tom Elliot
# 2013

# todo: check data passed in is only byte-size (check for > 256?)

from smbus import SMBus

class led:
	def __init__(self, bus, address):
		self.bus = SMBus(bus)
		self.address = address

	def setrgb(self, r, g, b):
		self.bus.write_byte(self.address, ord('n'))
		sendthreebytes(self.bus, self.address, r, g, b)
	
	def fadergb(self, r, g, b):
		self.bus.write_byte(self.address, ord('c'))
		sendthreebytes(self.bus, self.address, r, g, b)

	def fadehsb(self, r, g, b):
		self.bus.write_byte(self.address, ord('h'))
		sendthreebytes(self.bus, self.address, r, g, b)

	def faderandomrgb(self, r, g, b):
		self.bus.write_byte(self.address, ord('C'))
		sendthreebytes(self.bus, self.address, r, g, b)

	def faderandomhsb(self, r, g, b):
		self.bus.write_byte(self.address, ord('H'))
		sendthreebytes(self.bus, self.address, r, g, b)

	def playscript(self, n, r, p):
		self.bus.write_byte(self.address, ord('p'))
		sendthreebytes(self.bus, self.address, n, r, p)

	def stopscript(self):
		self.bus.write_byte(self.address, ord('o'))

	def setfadespeed(self, f):
		self.bus.write_byte(self.address, ord('f'))
		self.bus.write_byte(self.address, f)

	def settimeadjust(self, t):
		self.bus.write_byte(self.address, ord('t'))
		self.bus.write_byte(self.address, t)

	#def getrgbcolour(self):
		# ???

#	def writescript(self, n, p, ...)
#	def readscript(self, n, p	)

	def scriptlengthrepeats(self, n, l, r):
		self.bus.write_byte(self.address, ord('L'))
		sendthreebytes(self.bus, self.address, n, l, r)

#	def setaddress(self, a, ...)
#	def getaddress(self)

	def getfirmware(self):
		#self.bus.write_byte(self.address, ord('Z'))
		fw = bytearray()
		fw = self.bus.read_block_data(self.address, ord('Z'))
		print fw
	#	print chr(self.bus.read_byte(self.address))
	#	print chr(self.bus.read_byte(self.address))
		
	def startupparams(self, m, n, r, f, t):
		self.bus.write_byte(self.address, ord('B'))
		sendthreebytes(self.bus, self.address, m, n, r)
		self.bus.write_byte(self.address, f)
		self.bus.write_byte(self.address, t)
		
def sendthreebytes(bus, address, one, two, three):
	bus.write_byte(address, one)
	bus.write_byte(address, two)
	bus.write_byte(address, three)

