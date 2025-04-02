'''
Write a program to greet all the person names stored in a list ' l ' and which starts 
with A. 
l = ["Arbind","Aman","Aakash","Hari"] 

'''
l = ["Arbind","Aman","Aakash","Hari","Sashant","Mahi"]

for name in l:
    if(name.startswith("A")):
        print(f"Hello Mr. {name}")

