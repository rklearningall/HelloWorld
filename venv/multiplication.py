##  Write a program to accept a number from the user and print its multiplication table (upto “times 10”).

num = int(input("Enter the numbrs  "))
for i in range(1,21):
    print(num,'x',i,'=',num*i)

