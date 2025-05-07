'''Write a program to find out whether a file is identical & matches the content of 
another file.'''

with open("file.txt", "r") as f:
    content1 = f.read()

with open("file2.txt","r") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these filea are identical")

else:
    print("NO these files nare not identical")

