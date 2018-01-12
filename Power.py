def pow(a,b):
    c=1
    for i in range(b):
        c=a*c
    return c
a=raw_input().split(" ")
a=map(int,a)
print(pow(a[0],a[1]))
