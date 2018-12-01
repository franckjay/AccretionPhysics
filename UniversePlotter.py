import math
import cmath

uni= open('universe.txt', 'a')
paths= open('paths.txt', 'a')

def noBB(matter):
    ##Computes the BigBounce/Loitering Line
    lamb = 0    
    if matter > 0.5:     
        squiggles=math.cos((0.3333333333)*math.acos((1-matter)/matter))
        lamb = 4*matter*math.pow(squiggles,3)
    else:
        paren=(1-matter)/matter
        brackets = (0.333333333)*math.acosh(paren)
        squiggles=math.cosh(brackets)
        lamb = 4*matter*math.pow(squiggles,3)

    a=str(matter)
    b=str(lamb)
    c = a +"  "+ b + "\n"
    uni.write(str(c))   
    
    return lamb   
    

def dynState(matter):
    ##Accel/Decel
    lamb = 0.5*matter  

    a=str(matter)
    b=str(lamb)
    c = a +"  "+ b + "\n"
    uni.write(str(c))

    return lamb

def geometry(matter):
    ##Determines k
    lamb=1-matter

    a=str(matter)
    b=str(lamb)
    c = a +"  "+ b + "\n"
    uni.write(str(c)) 

    return lamb

def Expand(matter):

    if matter > 1:
        squiggles=(0.333333*math.acos((1-matter)/matter))+(1.33333*math.pi)
        stuff=math.cos(squiggles)
        lamb=4*matter*math.pow(stuff,3)
    else:
        lamb=0
    a=str(matter)
    b=str(lamb)
    c = a +"  "+ b + "\n"
    uni.write(str(c))

    return lamb

def universePlotter(m0Omega,lam0Omega):

    R=10.0
    while R > 0:

        totOmega= m0Omega+lam0Omega
        denom = (m0Omega/math.pow(R,3))+((1-totOmega)/math.pow(R,2))+lam0Omega
        mOmega =(m0Omega/math.pow(R,3))*(1/denom)
        lamOmega = lam0Omega/(denom)
        a=str(mOmega)
        b=str(lamOmega)
        c = a +"  "+ b + "\n"
        paths.write(str(c))
        R=R-0.001
        
    

    return lamOmega


##Builds the list of values to get the boundary lines
n=0.001
while n <= 10:
    
    noBB(n)
    dynState(n)
    geometry(n)
    Expand(n)       
    n+=0.001

##Iterates through the paths of the different compositions
matter=[1.0,0.2,0.3,0.1,1.3,0.5]
lamb=[0.0,0.0,0.7,0.8,0.6,1.5]


for i in range(len(matter)):
    universePlotter(matter[i],lamb[i])
    
    

uni.close()
paths.close()
