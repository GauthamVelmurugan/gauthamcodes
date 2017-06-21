def main():
    a=['a','e','i','o','u']
    b=str(raw_input("Enter a character to check it is vowel or consonant"))
    if b in a:
        print"The given character is a vowel"
    else:
        print"The given character is consonant"

if __name__ == '__main__':
    main()
