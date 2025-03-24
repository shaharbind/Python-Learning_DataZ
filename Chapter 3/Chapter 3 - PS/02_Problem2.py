# Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>","Arbind").replace("<|Date|>","23 Jun 1998"))
