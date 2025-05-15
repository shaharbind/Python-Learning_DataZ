#  Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 19
b = 22
c =3

print(f"The greatest number is {greatest(a,b,c)}")
    