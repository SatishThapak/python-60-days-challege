# Insert a Line at a Specific Position

# Step 1: Read all lines
with open("file.txt", "r") as file:
    lines = file.readlines()

# Step 2: Insert new line at index 2 (before "Line 3")
lines.insert(3, "Line 2.5: Inserted line\n")

# Step 3: Write back the modified content
with open("file.txt", "w") as f:
    f.writelines(lines)

# Verify
with open("file.txt", "r") as f:
    print(f.read())
