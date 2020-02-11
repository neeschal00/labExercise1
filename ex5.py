"""A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
The program should read three integers: the number of students in each of the three
classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10
desks. The second group has 21 students, so they can get by with no fewer than 11 desks."""

classA=int(input("Enter a number of students in first class:"))
classB=int(input("Enter a number of students in second class:"))
classC=int(input("Enter a number of students in third class:"))
per1=classA//2
per2=classB//2
per3=classC//2
t=per1 + per2 + per3
print("The total no. of desk to be purchased:" , t)