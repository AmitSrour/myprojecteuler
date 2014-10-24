def isPrime(number):
        x = number/2
        while x > 2:
                if number % x == 0:
                        return False
                x -=1
        return True
number = 600851475143  
#the largest of even is the number devided by 2(because 2 is the smaller)
devider = 2
largest = 1
while devider < number/2 :
        if number % devider == 0:
                if isPrime(devider):
                        print devider
                        if devider > largest:
                                largest = devider
        devider +=1
print ("The largest Prime factor is %s" % largest)
