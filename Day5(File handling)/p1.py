# Open a File on the Server
# The open() function returns a file object, which has a read() method for reading the content of the file:

file = open("file.txt")
print(file.read())

# If the file is located in a different location, you will have to specify the file path, like this:

# f = open("/home/qolsysjci/python-60-days-challege/README.md")
# print(f.read())

# we can also use the with statement when opening a file:
# Then you do not have to worry about closing your files, the with statement takes care of that.

with open("file.txt", "r") as f:
  print(f.read())

# If you are not using the with statement, you must write a close statement in order to close the file:

f = open("file.txt")
print(f.read())
f.close()

# Read Only Parts of the File
with open("file.txt") as f:
  print(f.read(2))
