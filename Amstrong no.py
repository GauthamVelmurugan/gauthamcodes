def pow(a,b):
    sum=1
    for i in range(b):
        sum=sum*a
    return sum
a=int(input())
b=[]
c=a
while a<>0:
    d=a%10
    b=b+[d]
    a=a/10
e=len(b)
sum=0
for i in b:
    sum=sum+(pow(i,e))
if c==sum :
    print"Yes"
else:
    print"No"
