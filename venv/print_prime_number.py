##  Write a program to accept the lower bound number and
## the upper bound number from the user and print the prime numbers between them.

lower_bound = int(input("Enter the lower bound number: "))
upper_bound = int(input("Enter the upper bound number: "))


for num in range(lower_bound, upper_bound + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num,end =" ")

print("\nPrime numbers between", lower_bound, "and", upper_bound)
