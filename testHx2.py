from hx711_2 import Hx711
a = Hx711(48,14)
abuf = []
a.tare(1)
a.set_scale(1)

while 1:
	print a.get_units(1)



