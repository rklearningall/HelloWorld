## Write a program to accept a number and determine whether it is a prime number or not.

num = int(input("enter the any  number "))
if num > 1:
 for i in range(2,num):
    if (num % i ) == 0:
        print(num,"is the not prime number ")
        break
 else:
     print(num, "is the prime number ")
else:
    print(num, "is the not prime number ")