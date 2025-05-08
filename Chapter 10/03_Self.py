class Employee:
    name = "Arbind"
    language = "Nepali"
    salary = 120000
    
    def getInfo(self): # Here we have created method self
        print(f"The name of employee is {self.name}. The salary of employee is {self.salary}")


    

a2 = Employee() # Here a2 is a object
a2.getInfo()

