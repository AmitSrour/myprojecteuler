def isPalindrome(N):
        if len(N) <= 1:
                return True
        if N[0] != N[-1]:
                return False
        return isPalindrome(N[1:-1])
largest = 1
for i in range(999,1,-1):
        for j in range(999,1,-1):
                n= i*j
                if isPalindrome(str(n)) and n > largest:
                        largest = n
                        print largest
                        

