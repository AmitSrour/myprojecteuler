import math
for a in range(1,1000):
    for b in range(1,1000-a):
        if 1000 == math.sqrt(a**2+b**2) + a+b:
            print("1000 = %d+%d+%d"% (a,b,math.sqrt(a**2+b**2)))
            print("and the product of abc is:",a*b*math.sqrt(a**2+b**2))
