## File Handling in Python
- File handling in Python allows you to create, read, write, and manage files such as .txt, .csv, or .json. It is essential for storing data permanently, processing large datasets, and automating tasks like configuration management.

## 1. Opening a File
- Use the open() function:
```python
file = open("example.txt", "r")  # 'r' = read mode
```
### Modes:

"r" → Read (default)
"w" → Write (creates new file or overwrites existing)
"a" → Append (adds content at end)
"b" → Binary mode (e.g., images, PDFs)
"x" → Create (fails if file exists)

## 2. Reading Files
- Read entire file:
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```
- Read line by line:
```python 
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```
## 3. Writing to Files
- Overwrite content:
```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
```
- Append content:
```python
with open("example.txt", "a") as file:
    file.write("This is appended text.\n")
```
## 4. Closing Files
- Always close files after use:
```python
file.close()
```
- Or use with open(...) which auto-closes the file.

## 5. Useful Methods

**read()**	        Reads entire file
**readline()**	    Reads one line
**readlines()**	    Reads all lines into a list
**write()**     	Writes string to file
**writelines()**	Writes list of strings

## Read Only Parts of the File
- By default the read() method returns the whole text, but you can also specify how many characters you want to return:

```python
with open("file.txt") as f:
  print(f.read(5))
```
## Write to an Existing File
- To write to an existing file, you must add a parameter to the open() function:
- "a" - Append - will append to the end of the file
- "w" - Write - will overwrite any existing content

```python
with open("file.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("file.txt") as f:
  print(f.read())
  ```
## 6. Create a New File
- To create a new file in Python, use the open() method, with one of the following parameters:
1. "x" - Create - will create a file, returns an error if the file exists
2. "a" - Append - will create a file if the specified file does not exists
3. "w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "x")

## 7. Delete a File
- To delete a file, you must import the OS module, and run its os.remove() function:
```python
import os
os.remove("demofile.txt")
```
Check if file exists, then delete it:

```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

## Delete Folder
- To delete an entire folder, use the os.rmdir() method:

```python
import os
os.rmdir("myfolder")
```

# Note: You can only remove empty folders.

--

