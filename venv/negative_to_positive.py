# Write a program to accept a number, if it is negative then covert it to a positive number.

# num = int(input(" Enter the number "))
# print(abs(num))

num = float(input("Enter the number  "))

if num < 0:
    num = -num
print("The absolute value of the number is:", num)