import math

data = open('H2.txt', 'r')
restData = open('zH2.txt', 'w')
##Grabs the data from the file and places each variable in an array
wavelength = []
flux = []
for i in data:
    i=i.split()
    wavelength.append(i[0])
    flux.append(i[1])

##Calculates Redshift
Halpha = 6668.29
restAlpha=6562.8
rShift = (Halpha-restAlpha)/restAlpha
print "The measured redshift of this object is : ",rShift

##Shifts each data point in the set
n=0
for i in wavelength:
    rest = float(i)/(rShift+1)
    a = str(rest) + "   " + str(flux[n]) + "\n"
    restData.write(a)
    n+=1


data.close()
restData.close()
