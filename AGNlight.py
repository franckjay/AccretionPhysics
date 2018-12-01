import math
import random


Xdat=open('xdat1.txt', 'w')
def randomWalk(z,X,JD):

    alpha = 0.0
    Xi = (alpha*X)+z + 5
    c = 2460000-JD
    a = str(c) + "  " + str(Xi) + '\n'
    Xdat.write(a)

    return Xi








JD= 2455675
n= 0 
X= 1
while n < 2500:
    z=random.uniform(-1,1)
    X = randomWalk(z,X,JD)
    n+=12.5
    JD+=12.5
    
