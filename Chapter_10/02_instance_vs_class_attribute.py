class Employee:
    name = "Arbind"
    language = "Nepali"
    salary = 120000


a2 = Employee() # Here a2 is a object
a2.language = "English" # Here we created instance objects 

print(a2.name,a2.language, a2.salary)


# English will print because instance attribute is more preferance than class attribute
