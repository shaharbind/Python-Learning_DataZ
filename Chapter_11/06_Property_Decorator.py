class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self,value):
        self.ename= value

b = Employee()

b.a = 55

b.name = "Arbind"
print(b.name)