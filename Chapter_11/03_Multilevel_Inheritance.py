class Employee:
    a= 20

class Programmer(Employee):
    b = 3

class Manager(Programmer):
    c = 44


obj = Employee()
print(obj.a)

obj = Manager()

print(obj.a, obj.b, obj.c)