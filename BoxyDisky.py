import math

plot = open('Boxy-d.txt', 'w')
theta = 0
a0 = 30
e = 0.4
##
a2 = a0 * e

a = 0
while theta < 360:
    a = a0 + a2*math.cos(2*theta) - 0.1*a0*math.cos(4*theta) 
    x = a*math.sin(theta)
    y = a*math.cos(theta)
    st = str(y) + "   " + str(x) + "\n"
    plot.write(st)
    theta +=0.001



plot.close()
