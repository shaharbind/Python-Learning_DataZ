'''Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?'''

class Demo:
    a = 7


obj = Demo()
print(obj.a) # Here it prints the class attribute because instannce attribute is not present

obj.a = 0 # Here i have set instance attribute

print(obj.a) # Here i prints the class attribute because instannce attribute is present

print(Demo.a)

# So no change in class attribute