# Overwrite Existing Content

with open("file.txt", "w") as f:
    f.write("This will replace all previous content.")

# Read the file after overwriting
with open("file.txt", "r") as f:
    print(f.read())
