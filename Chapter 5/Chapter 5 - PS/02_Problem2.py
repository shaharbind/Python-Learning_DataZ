'''Write a program to input eight numbers from the user and display all the unique 
numbers (once). '''

s = set() # An empty set

n = input("Enter number 1: ")
s.add(int(n))

n = input("Enter number 2: ")
s.add(int(n))

n = input("Enter number 3: ")
s.add(int(n))

n = input("Enter number 4: ")
s.add(int(n))

n = input("Enter number 5: ")
s.add(int(n))

n = input("Enter number 6: ")
s.add(int(n))

n = input("Enter number 7: ")
s.add(int(n))

n = input("Enter number 8: ")
s.add(int(n))

print(s)