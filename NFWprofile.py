import math


r1 = 50.0
r2 = 230.0
p1 = 1.0E6
p2 = 3.7E4

pratio = p1/p2

dp = 1e10
a= 70.0
pbest=0.0
while a < 85.0:
    x =r2/a
    z = r1/a
    num = x*math.pow((1+x),2)
    den = z*math.pow((1+z),2)
    p = num/den
    diff = abs(p-pratio)
    
    if diff < dp:
        dp = diff
        pbest = p
        abest = float(a)
    a+=.00001


print "Best :",pbest
print "dp: ",dp
print 'abest: ',abest
    

    

