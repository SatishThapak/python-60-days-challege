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
