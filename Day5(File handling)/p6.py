# Create a new file called "myfile.txt"
with open("myfile.txt", "x") as f:
    pass   # file is created, nothing written



# Remove the file safely
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File deleted successfully")
else:
    print("The file does not exist")
