from hx711 import Hx711
a = Hx711(48,14)
while 1:
	print a.read()


