# Write a program to find whether a given number is prime or not.

# By using for loop

n1 = int(input("Enter a number: "))

for i in range(2,n1):
    if(n1%i)==0:
        print("Number is not a prime")
        break
    
else:
    print("Number is a prime")


# B y using while loop


        