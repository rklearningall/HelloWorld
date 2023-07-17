## Write a program to accept a number and find its factorial


num = int(input("Enter the number  "))
factorial = 1
if num <= 0:
    print("sorry factorial does not exists for negative numbers ")
elif num == 1:
    print("the factorial of 0 is 1 ")
else:
   for i in range(1, num + 1):
        factorial = factorial * i
   print("the factorial ",num,"is",factorial)