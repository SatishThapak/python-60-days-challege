# Write to an Existing File

with open("file.txt", "a") as f:
    f.write("\nNow the file has more content!")
 
#open and read the file after the appending:
with open("file.txt") as f:
  print(f.read())