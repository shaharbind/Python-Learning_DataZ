'''
Create an empty dictionary. Allow 4 friends to enter their favorite name as 
value and use key as their names. Assume that the names are unique. 

'''
dict1 = {}
name = input("Enter friends name: ")
lang = input("Enter Language: ")

dict1.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language: ")

dict1.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language: ")

dict1.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter Language: ")

dict1.update({name:lang})

print(dict1)