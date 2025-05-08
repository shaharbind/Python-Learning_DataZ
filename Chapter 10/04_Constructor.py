class Employee:
    name = "Arbind"
    language = "Nepali"
    salary = 120000
    
    def getInfo(self): # Here we have created method self
        print(f"The name of employee is {self.name}. The salary of employee is {self.salary}")

    def __init__(self): # Here we created dunder method which is automatically called 
        print("I am creating an object")

amar = Employee()
amar.getInfo()
print(amar.name,amar.salary)

