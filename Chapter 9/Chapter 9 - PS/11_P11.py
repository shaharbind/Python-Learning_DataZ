#  Write a python program to rename a file to “renamed_by_ python.txt.

with open("rename1.txt", "r") as f:
        content = f.read()



with open("renamed_by_ python.txt", "w") as f:
        content = f.write(content)

