## Write a program to accept the following details of an employee: empno, name and monthly salary;
# calculate the yearly salary and display the result.

empno = int(input("Enter the employe no "))
name = input("enter the employe name ")
monthly_salary = float(input("enter the monthly salary "))

year_salary = monthly_salary * 12

print("\nemployee id is",empno ,"\nemployee name is ",name,"\nmonthly salary",monthly_salary,"\nyear_salary",year_salary)