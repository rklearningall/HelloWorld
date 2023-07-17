##  Write a program to accept the marks scored in three subjects;
## determine the sum and average of the entered marks.
## Grade is awarded based on following criteria.

subject1 = int(input("Enter The first subject "))
subject2 = int(input("Enter The second subject "))
subject3 = int(input("Enter The third subject "))
Total = subject1 + subject2 + subject3
avg = Total / 3
print("Total" ,Total)
print("avg" ,avg)
if avg <= 35:
    print("Grade D")
elif avg <= 60:
    print("Grade B")
else:
    print("Grade A")