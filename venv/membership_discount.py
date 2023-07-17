##  In a shopping mall, privileged customers (if they have a membership card) are being given a 10%
## discount on the billed amount, and the others are being given a 3% discount.
## Write a program to accept the billing amount and confirm the membership card from the customer;
## #calculate and display the net amount to be paid by the customer.


bill = int(input("enter the amount "))
user_input = input("Do you have membership in mall (y/n) ")
if user_input == 'y':
    dis = 0.10 * bill
    net_bill = bill - dis
    print("Thank you! Your total bill amount is Rs",bill, "discount is Rs ",dis,
          " and net amount payable is Rs" ,net_bill)
elif user_input =='n':
    dis = 0.03 * bill
    net_bill = bill - dis
    print("Thank you! Your total bill amount is Rs",bill, "discount is Rs ",dis,
          "and net amount payable is Rs" ,net_bill)