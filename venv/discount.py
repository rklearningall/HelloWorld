##  Write a program to accept the billing amount,
# if it is > 6000 then give a discount of 10% and display the net amount.

amount = float(input("Enter the bill amount  "))

if amount > 6000:
    dis = 0.10 * amount
    net_amount = amount -dis
else:
    net_amount = amount
print("total to be paid by customer ",net_amount )
