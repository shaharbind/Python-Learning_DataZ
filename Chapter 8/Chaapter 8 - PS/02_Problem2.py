# Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f(c):
    F = (c * 9/5) + 32
    return F

c = float(input("Enter temperature: "))
print(f"The temperature in Fahrenheit is {c_to_f(c)}")
