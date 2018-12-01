import math

MassRadius= open('MassRadius.txt', 'w')
velRadius= open('velRadius.txt', 'w')


R = 0.01
M= 0.0
v=0.0
k = 9.58E5
BH = 3.7E6
G= 6.67E-11
while R <= 1000:
    M = (k*R) + BH
    c = G*(6.19E19 + ((1.99E30*BH)/(3.086E16*R)))
    v = math.pow(c,0.5)/1000
    if v < (2*64.38):
        print R
    a = str(math.log(R, 10)) + "   " + str(math.log(M,10)) + '\n'
    b = str(math.log(R, 10)) + "   " + str(v) + '\n'
    MassRadius.write(a)
    velRadius.write(b)
    R += 0.001









MassRadius.close()
velRadius.close()
