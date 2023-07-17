##  Write a program to accept 3 numbers from the user and find the biggest of them.

num1 = int(input("Enter The  Number 1 "))
num2 = int(input("Enter The Number 2 "))
num3 = int(input("Enter The Number 3 "))
if num1 > num2 and num1 > num3:
    print(num1," is bigger of given numbers ")
elif num2 > num3:
    print(num2," is bigger of given numbers")
else:
    print(num3," is bigger of given number ")