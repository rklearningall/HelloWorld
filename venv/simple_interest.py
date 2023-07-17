## Write a program to accept the principal amount, rate of interest, time and calculate the simple interest.

amount = float(input("Enter the principal amount " ))
rate = float(input("Enter the rate of interest "))
time = float(input("Enter the time "))

si = amount * rate * time / 100
print("simple interest of given amount is  ",si)