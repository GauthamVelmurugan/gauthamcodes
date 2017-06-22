#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GauthamVelmurugan
#
# Created:     22-06-2017
# Copyright:   (c) GauthamVelmurugan 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=int(raw_input("Enter a number"))
    sum=0
    for i in range(1,a+1):
        sum=sum+i
    print"Sum of N numbers is :",sum


if __name__ == '__main__':
    main()
