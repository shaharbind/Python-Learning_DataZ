# Attempt problem 1 using while loop. 

# Problem 1 : Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter the number: "))

i = 1

while(i<11):
    print(f"{number} x {i} = {number*i}")
    i = i+1