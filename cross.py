##Klein Neshina Cross Section with different limits
import math
cross= open('cross.txt', 'w')

def crossSection(eps):
    ##Electron Radius(Thomson Scattering Length)
    r=2.8179E-13

    brackets=1-((2*eps+2)/math.pow(eps,2))
    squiggles = (brackets*math.log(2*eps+1))+(1.0/2.0)+(4.0/eps)-(1/(2*math.pow((2*eps+1),2)))
    sigma = ((math.pi*math.pow(r,2)/eps)*squiggles)

    a=str(eps)
    b=str(sigma)
    c = a +"  "+ b + "\n"
    cross.write(str(c))
    
    return eps


eps = 1e-5
while eps <= 1:
    crossSection(eps)
    eps+= .001

while eps <= 1e4:
    crossSection(eps)
    eps+= .1

while eps <= 1e7:
    crossSection(eps)
    eps+= 10






cross.close()
