import mraa

class Hx711:
	def __init__(self,dout,pd_sck, gain = 128):
		# self.PD_SCK = pd_sck
		# self.DOUT = dout
		self.PD_SCK = mraa.Gpio(pd_sck)
		self.DOUT = mraa.Gpio(dout)
		self.PD_SCK.dir(mraa.DIR_OUT)
		self.DOUT.dir(mraa.DIR_IN)
		self.GAIN = 1
		self.OFFSET = 0
		self.SCALE = 1
		self.set_gain(gain)
	def set_gain(self,gain):
		if gain == 128:
			self.GAIN = 1
		elif gain == 64:
			self.GAIN = 3
		elif gain == 32:	
			self.GAIN = 2
		self.PD_SCK.write(0) # is for low signal 
		self.read()
	def read(self):
		while self.DOUT.read() == 1:
			continue

		value = 0
		data = 0
		filler = 0x00
		for i in range(24):
			self.PD_SCK.write(1)
			value = value<<1
			self.PD_SCK.write(0)
			if(self.DOUT.read()):
				value = value + 1
		self.PD_SCK.write(1)
		value = value ^ 0x800000
		self.PD_SCK.write(0)
		return value	

	def read_average(self,times):
		sum0 = 0
		for i in range(times):
			sum0 += self.read()
		return sum0/times;
	

	def get_value(self,times):
		return self.read_average(times) - self.OFFSET

	
	def get_units(self,times):
		return self.get_value(times) /self.SCALE

	
	def tare(self, times):
		sum = self.read_average(times)
		self.set_offset(sum)

	def set_scale(self,scale):
		self.SCALE =scale

	def get_scale(self):
		return self.SCALE

	def get_offset(self):
		return self.OFFSET

	

	def set_offset(self,offset):
		self.OFFSET = offset;

	def power_down(self):
		self.PD_SCK.write(0)
		self.PD_SCK.write(1)

	def power_up(self):
		self.PD_SCK.write(0)
	

	# def shiftIn(self):
	# 	value =0
	# 	for i in range(24):
	# 		self.PD_SCK.write(1)
	# 		value = value<<1
	# 		self.PD_SCK.write(0)
	# 		if(self.DOUT.read()):
	# 			value = value + 1

	# 	return value

	# def is_ready(self):
	# 	if self.DOUT.read() == 0:
	# 			return True
	# 	else:
	# 		return False
