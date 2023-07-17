##  Write a program to accept two numbers num1 and num2; when one is subtracted from the other,
## the result should always be a positive number.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 >= num2:
    result = num1 - num2
else:
    result = num2 - num1

print("The result is:", result)






