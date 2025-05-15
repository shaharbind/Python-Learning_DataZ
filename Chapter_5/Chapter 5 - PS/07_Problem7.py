'''
If the names of 2 friends are same; what will happen to the program in problem 
6?
'''
# Than it will skip the first name 
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