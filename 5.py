def isDevisble(N, d): ## checks to see if N devisble evenly by all between d-0
    if N % d != 0:
        return False
    if d == 1:
        return True
    return isDevisble(N,d-1)

i = 1
while True:
    if isDevisble(i*20,20):
        print i*20
        break
    i+=1
    
