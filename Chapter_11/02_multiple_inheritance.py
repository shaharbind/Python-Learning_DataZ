class Employee:
    company = "Dialsewa"
    name = "Arbind"
    def show(self):
        print(f"The name of employee is {self.name} and his company name is {self.company}")
    


class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Here your language is {self.language}")
    

class Programmer(Employee, Coder):
    company = "MistriSewa"
    def showLanguage(self):
        print(f"The name is {self.name } , He now worked in {self.company} and he is familiar with {self.language}")


a = Employee()
b = Programmer()
a.show()
b.show()

b.showLanguage()
b.printLanguage()