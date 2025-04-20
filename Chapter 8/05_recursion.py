'''
factorial(0) = 1
factorial(1) = 1
factoriral(2) = 2 x 1
factoriral(3) = 3 x 2 x 1
factoriral(4) = 4 x 3 x 2 x 1
factorial (5) = 5 x 4 x 3 x 2 x 1
factorial (n) = n x n-1 x ...............3 x 2 x 1
factorial (n) = n x factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number:"))

print(f"factorial of number is : {factorial(n)}")
