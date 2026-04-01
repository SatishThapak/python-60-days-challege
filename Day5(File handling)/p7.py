import os

folder_name = "myfolder"
file_name="myfolder/mytext.txt"

# Check if the folder exists
if not os.path.exists(folder_name):
   os.makedirs(folder_name)
   print(f"Folder '{folder_name}' created successfully.")
else:
   print(f"Folder '{folder_name}' already exists.")

# Step 2: Create a file inside the folder
with open(file_name, "w") as f:
    f.write("Hello, this is a test file.")
print(f"File '{file_name}' created successfully.")


# Step 3: Delete the file safely
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")
else:
    print("The file does not exist.")