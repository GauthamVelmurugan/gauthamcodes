def main():
    import sys
    A=str(raw_input("Enter a string"))
    B=len(A)
    c=range(B)
    j=0
    if(B%2==0):
        for i in range(B/2):
            c[j]=A[j+1]
            j+=1
            c[j]=A[j-1]
            j+=1
    else:
        for i in range(B/2):
            c[j]=A[j+1]
            j+=1
            c[j]=A[j-1]
            j+=1
        c[j]=A[j]
    for k in range(B):
        sys.stdout.write(""+str(c[k]))
