from hx711 import Hx711
a = Hx711(36,20)
abuf = []
while 1:
	abuf = []
	for i in range(10):
		abuf.append(a.read())
	
	abuf.sort()
	string = str()
	for i in range(10):
		string = string  +  str(abuf[i]) + " "
	
	aval = (abuf[4] + abuf[3] + abuf[5] + abuf[6])/4	
	print aval
	print string
