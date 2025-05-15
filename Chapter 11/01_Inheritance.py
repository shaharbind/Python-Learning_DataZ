class Employee:
    company = "Dialsewa"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary of employee is {self.salary}")



class Programmer(Employee):
    company = "MistriSewa"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language} language")
    


a = Employee()
b = Programmer()

print(a.company, b.company)
