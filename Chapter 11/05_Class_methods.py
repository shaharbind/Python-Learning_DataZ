class Employee:
    a = 1
    @classmethod # If we use class method than class attributes of a will print which is 1 not 455
    def show(cls):
        print(f"The value of a is {cls.a}")
    

e = Employee()

e.a = 455
e.show()