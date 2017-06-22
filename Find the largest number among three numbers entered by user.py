def main():
    a=range(3)
    for i in range (3):
        a[i]=int(raw_input("Enter the"+str(i+1)+" number"))
    if a[0]>a[1]:
        if a[0]>a[2]:
            print"The greatest nmber is :",a[0]
        else:
            print"The greatest number is :",a[2]
    elif a[1]>a[2]:
        print"The greatest number is :",a[1]
    else:
        print"The greatest number is :",a[2]

if __name__ == '__main__':
    main()
