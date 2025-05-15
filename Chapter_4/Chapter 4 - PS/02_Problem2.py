''' Write a program to accept marks of 6 students and display them in a sorted 
manner. '''

# Write a program to store seven Marks in a list entered by the user. 

Marks = []

f1 = int(input("Enter Marks here: "))
Marks.append(f1)
f2 = int(input("Enter Marks here: "))
Marks.append(f2)
f3 = int(input("Enter Marks here: "))
Marks.append(f3)
f4 = int(input("Enter Marks here: "))
Marks.append(f4)
f5 = int(input("Enter Marks here: "))
Marks.append(f5)
f6 = int(input("Enter Marks here: "))
Marks.append(f6)
f7 = int(input("Enter Marks here: "))
Marks.append(f7)

Marks.sort()
print(Marks)

# Not sorted because it in in string form or because it takes int(input in string fornm)