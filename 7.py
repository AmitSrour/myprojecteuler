primes = [2]
def isPrime(testSubject):

    global primes
    for i in primes:
        if testSubject % i == 0 :
            return False
    primes.append(testSubject)
    print "pretty much a prime, appended: ", testSubject
    return True

j=3
while len(primes)+1 != 10002:

    if isPrime(j):
        print "place:",len(primes) ## starting from 0 :(
    j+=1
    
