## Write a program to generate the first 'N' natural numbers. Accept the value of 'N' from the user.

num = int(input("Enter The Number "))
for i in range(1, num + 1):
    print(i, end=" ")