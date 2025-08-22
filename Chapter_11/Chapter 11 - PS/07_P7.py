'''Override the __len__() method on vector of problem 5 to display the dimension of the 
vector. '''

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
        return f"Vectro({self.x},{self.y},{self.z})"
    


    def __len__(self):
        return 4
    

v1 =vector(1,4,5)
v2 = vector(4,4,4)

print(len(v1+v2))

# Completed Chapter - 11,Inheritance and OOPS in Python