def isPrime(a):
    count=0
    for i in range(2,a):
        if(a%i==0):
            count=count+1
    if count==0:
        return True
    else:
        return False
a=raw_input().split(" ")
a=map(int,a)
for i in range(a[0]+1,a[1]):
    if isPrime(i):
        print i,
