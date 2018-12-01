import math
import numpy as np
import matplotlib.pyplot as plt

def rWD(mass,mu):
    mass = float(mass)
    mu=float(mu)
    chM = (5.816/(math.pow(mu,2)))
    mRatio = mass/chM
    a = 1-(math.pow(mRatio,1.33333))
    rad = 699500*(0.0225/mu)*math.sqrt(a)/math.pow(mRatio,(.333333333))
    return rad

mass = []

a = 0.4
while a <=1.45:
    mass.append(a)
    a+=.001


H=[]    
He=[]
C=[]
O=[]


for i in mass:
    m = float(i)
    H.append(rWD(m,1.008))
    He.append(rWD(m,2.002))
    C.append(rWD(m,2.001))
    O.append(rWD(m,2.000))


plt.title('Radius vs. Mass for WDs of differing composition.')
plt.ylabel('Radius (km)')
plt.xlabel('Mass M(sun)')
plt.text(0.8,10000, r'$\mu=2.002,2.001,2.000$ corresponding to He,C,O WDs')

plt.errorbar(0.48, 8850, xerr=0.02, yerr=606)
plt.errorbar(1.053, 5130, xerr=0.028, yerr=470)
plt.plot([mass],[He],'r.',[mass],[C],'b,',[mass],[O],'g*')
plt.show()
