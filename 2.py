first = 1
second = 2
next = 3
sum = 0

while second < 4000001:
        next = first + second
        print ("%s,") % first
        first = second
        second = next
        if first%2 == 0:
                sum +=first
print ("sum = %s" % sum)
                
                

