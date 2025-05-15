d = {} # empty dict

marks = {
    "Arbind" : 100,
    "Aman" : 55,
    "Hari" : 99,
    "list" : [10,20,30,40]
    
}
print(marks.items())
print(marks.keys())
marks.update({"Arbind":99}) # To update data in dict or to add data keys values in dict
print(marks)

print(marks.get("Aman"))


