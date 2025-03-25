'''
Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}

'''

s = {8, 7, 12, "Harry", [1,2]}

s.update([1,2],[4,7])

print(s)

'''
No, you cannot change the values inside the list [1,2] 
because sets do not allow mutable (changeable) elements like lists.

'''