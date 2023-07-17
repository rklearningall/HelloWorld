# The Sports Club registration form has the following details: name, mobile number and age.
# Per the membership policy, the person should be at least 18 years old to become a member.
# Write a program to accept the details mentioned above;
# if the age is >18 years then display the entered details with a congratulatory message,
# else the following message should be displayed “Sorry! You need to be at least 18 years old to get membership.


name = str(input("entrt the your full Name "))
phone = int(input("enter the your full moblic number "))
age = int(input("enter your ages "))
if age < 18:
   print("Sorry! You need to be at least 18 years old to get membership.")
else:
   print("Congratulations",name," for your successful registration.")
