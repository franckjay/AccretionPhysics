import math

a = open("TempRadiusNS.dat", 'a')

def Tr(r):

    R=(1E6/r)
    T4 = (3.89E45/(math.pow(r,3)))*(1-math.sqrt(R))
    T = math.pow(T4,0.25)

    z=str(R)
    y=T
    x=str(y)
    d = z + "    " + x + "\n"
    a.write(str(d))
    
    return T

r = 1E6

while r < 1E10:
    l = Tr(r)
    r+=0.1E6


while r < 1E14:
    l = Tr(r)
    r+=1E10


a.close()


