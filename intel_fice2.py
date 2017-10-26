from hx711 import Hx711
from time import sleep
calibration_factor = -17650.0 # set the calibratino factor from -7050 for pounds to -176550 for kg's
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
        
        w = r1 + r2
        if w > threshold_w:
                x = (r1*l1 + r2*l2)/w

                if  w-w_p > threshold_w or w_p-w > threshold_w or x-x_p > threshold_x or x_p-x > threshold_x : 
                        w_n = w - w_p
                        x_n = (w*x - w_p*x_p)/w_n

                        for i in range(6):
                                if x_n < borders[i]:
                                        if w_n > 0:
                                                mark[i] =  w_n # replacing 1 with the weight added
                                                mark2[i] = 1
                                                print "Container Added at : " + str(i + 1)
                                        elif w_n < 0:
                                                mark2[i] = 0
                                                mark[i] = 0
                                                print "Container Removed from : " + str(i+1)
                                        break

        else:
                for i in range(6):
                        mark2[i] = 0
                        mark[i] = 0.0 # not sure about this slot
                x = 0
	w_p = w
	x_p = x
        string = str()
        string2 = str()
        for i in range(6):
                string = string + str(mark[i]) + " "
                string2 = string2 + str(mark2[i]) + " "
        print string
        print string2
	with open('weights.txt','w') as w:
		w.write(string)
	

        a1.power_down()
        a2.power_down()
        sleep(1)
        a1.power_up()
        a2.power_up()


