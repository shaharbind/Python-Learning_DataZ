'''Create a class “Programmer” for storing information of few programmers 
working at Microsoft. '''

class Programmer:
    company = "Microsoft"
    name = "Arbind"
    salary = 12000

    def __init__(self,pin):
        self.pin = pin

    
a1 = Programmer(12)

print(a1.name, a1.company,a1.salary,a1.pin)
