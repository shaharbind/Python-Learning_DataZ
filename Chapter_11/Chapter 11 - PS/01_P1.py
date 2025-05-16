'''Create a class (2-D vector) and use it to create another class representing a 3-D 
vector.'''

class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self, i , j, k):
        super().__init__(i, j) # Here i used super keyboard to call i and j directly
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

        
a = TwoDvector(3,5)
a.show()
b = ThreeDvector(4,5,6)
b.show()