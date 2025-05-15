class Employee:
    def __init__(self):
        print("This is employee method")
    a= 20

class Programmer(Employee):
    def __init__(self):
        print("This is programmer method")
    b = 3

class Manager(Programmer):
    def __init__(self):
        super().__init__() # To call  all constructor method
        print("This is manager method")
    c = 44


obj = Employee()
obj = Manager()

print(obj.a, obj.b, obj.c)