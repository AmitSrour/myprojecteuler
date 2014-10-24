x = 0
for i in range(1,101): ##square of sums
    x += i
    print ("%d +%d = " % (x, i))
print (" square of sums:")
print x**2
y = 0
for i in range(1,101):##sums of squars
    y+= i**2
print y
print (x**2)-y
    
