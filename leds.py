# implements commands for BlinkM module
# Tom Elliot
# 2013

# todo: check data passed in is only byte-size (check for > 256?)


class led:
	def __init__(self, bus = 1, addr = 0x09):
		from smbus import SMBus
		self.bus = SMBus(bus)
		self.addr = addr

	def setrgb(self, r, g, b):
		sendbytes(self.bus, self.addr, ord('n'), r, g, b)
	
	def fadergb(self, r, g, b):
		sendbytes(self.bus, self.addr, ord('c'), r, g, b)

	def fadehsb(self, r, g, b):
		sendbytes(self.bus, self.addr, ord('h'), r, g, b)

	def faderandomrgb(self, r, g, b):
		sendbytes(self.bus, self.addr, ord('C'), r, g, b)

	def faderandomhsb(self, r, g, b):
		sendbytes(self.bus, self.addr, ord('H'), r, g, b)

	def playscript(self, n, r, p):
		sendbytes(self.bus, self.addr, ord('p'), n, r, p)

	def stopscript(self):
		sendbytes(self.bus, self.addr, ord('o'))

	def setfadespeed(self, f):
		sendbytes(self.bus, self.addr, ord('f'), f)

	def settimeadjust(self, t):
		sendbytes(self.bus, self.addr, ord('t'), t)

	#def getrgbcolour(self):
		# ???

#	def writescript(self, n, p, ...)
#	def readscript(self, n, p	)

	def scriptlengthrepeats(self, n, l, r):
		sendbytes(self.bus, self.addr, ord('L'), n, l, r)

#	def setaddr(self, a, ...)
#	def getaddr(self)

	def getfirmware(self):
		sendbytes(self.bus, self.addr, ord('Z'))
		print readbytes(self.bus, self.addr, 2)
	#	print chr(self.bus.read_byte(self.address)) 
	#	print chr(self.bus.read_byte(self.address)) 
		
	def startupparams(self, m, n, r, f, t):
		sendbytes(self.bus, self.addr, ord('B'), m, n, r, f, t)
	
def sendbytes(bus, addr, *bytes):
	for byte in bytes:
		bus.write_byte(addr, byte)
	
def readbytes(bus, addr, nb_bytes):
	for i in range(nb_bytes):
		yield bus.read_byte(addr, byte)
