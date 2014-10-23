sum=0
x=0
thresh=1000
while x < thresh:
        if x%3==0:
                print ("got into x%3==0")
                print ("the X that multiplies by 3 is %s") % x
                sum= sum+x
                print("New sum=%s" % sum)
        else:
                if x%5==0:
                        print ("got into x%5==0")
                        print ("the X that multiplies by 5 is %s") % x
                        sum= sum+x
                        print("New sum=%s" % sum)
        x+=1
print sum
