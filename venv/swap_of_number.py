## Write a program to accept two numbers from the user, swap their values and display the result.

num1= int(input("Enter the first number "))
num2= int(input("Enter the second number "))
print("before swaping number ",num1,num2)
num1 , num2 = num2 , num1
print("after swaping number is ",num1,num2)