def main():
    import string
    a=str(raw_input("Enter a character to check whether it is alphabet or not"))
    b=string.lowercase[:26]
    c=string.uppercase[:26]
    if a in b or c:
        print"The give character is alphabet"

    else:
        print"The given chaacter is not an alphabet"

if __name__ == '__main__':
    main()
