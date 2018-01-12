def pow(a,b):
    sum=1
    for i in range(b):
        sum=sum*a
    return sum
a=raw_input().split(" ")
a=map(int,a)
for i in range(a[0]+1,a[1]):
    b=[]
    c=i
    while c<>0:
        d=c%10
        b=b+[d]
        c=c/10
    e=len(b)
    sum=0
    for j in b:
        sum=sum+(pow(j,e))
    if i==sum :
        print i,
