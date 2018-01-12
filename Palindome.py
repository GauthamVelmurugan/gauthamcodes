a=int(input())
b=a
sum=0
while a!=0:
    d=a%10
    sum=sum*10+d
    a=a/10
if sum==b:
    print("Yes")
else:
    print("No")
