from hx711 import Hx711
from time import sleep
calibration_factor = -7050.0
a1 = Hx711(36,20)
a2 = Hx711(48,14)
a1.set_scale(calibration_factor)
a2.set_scale(calibration_factor)
a1.tare(1)
a2.tare(1)
borders = [10,20,30,40,50,60]
l1 = 5
l2 = 55
threshold_w = 1.0
threshold_x = 4
x  =float()
w = float()
x_p = 0.0
w_p = 0.0
x_n = float()
w_n = float()
mark = [0.0,0.0,0.0,0.0,0.0,0.0] # places on the shelf for containers
mark2 = [0,0,0,0,0,0]
while 1:
        arr = []
        arr2 = []
        for i in range(10):
                arr.append(a1.get_units(1))
                arr2.append(a2.get_units(1))
        arr.sort()
        arr2.sort()
        
        r1 = (arr[6]+ arr[5] + arr[3] + arr[4])/4
        r2 = (arr2[6] + arr2[5] + arr2[3] + arr2[4])/4
        
        print str(r1) +  "   " + str(r2)

        a1.power_down()
        a2.power_down()
        sleep(1)
        a1.power_up()
        a2.power_up()


