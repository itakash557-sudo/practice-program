x = int(input("Enter a number:"))
#Case 1 Negative numbers are not palindrome
if x < 0:
    print(False)
else:
    #Case 2 Convert to string and check palindrome
    if x>0:
        str(x)[::-1]
        print(True)
    else:
        print(False)

