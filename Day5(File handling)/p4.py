# Replace a Specific Line

# Step 1: Read all lines
with open("file.txt", "r") as f:
    lines = f.readlines()

# Step 2: Modify a specific line (index starts at 0)
lines[1] = "Line 2: Overwritten!\n"

# Step 3: Write back the modified content
with open("file.txt", "w") as f:
    f.writelines(lines)

# Verify
with open("file.txt", "r") as f:
    print(f.read())
