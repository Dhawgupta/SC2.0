from hx711 import Hx711
a = Hx711(48,14)
abuf = []
offset = 0 #8278500.0
div = 1  #18000.0
while 1:
	abuf = []
	for i in range(10):
		abuf.append(a.read())
	
	abuf.sort()
	string = str()
	for i in range(10):
		string = string  +  str(abuf[i]) + " "
	
	aval = (abuf[4] + abuf[3] + abuf[5] + abuf[6])/4	
	print ( aval - offset)/div
	print string



