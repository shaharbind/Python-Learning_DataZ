''' Write __str__() method to print the vector as follows: 
7i + 8j +10k  '''

''' Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them. '''

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)

    
        return result
    
    def __str__(self):
        return f"Vectro({self.x}i + {self.y}j + {self.z}k)"
    
v1 =vector(1,4,5)
v2 = vector(4,4,4)

print(v1+v2)