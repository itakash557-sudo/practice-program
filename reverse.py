#Getting input from user 
x = int(input("Enter the number to reverse:"))
#we use if elif else statement 
#case 1 and case 3 satisfied in if statement
if x > 0:
    reversed_num = int(str(x)[::-1])  
#case 2 is satisfied
elif x < 0:
    reversed_num = -int(str(abs(x))[::-1])
#user entered invalid number(eg:0) it returns 0
else:
    reversed_num = 0

print("Reversed:", reversed_num)
