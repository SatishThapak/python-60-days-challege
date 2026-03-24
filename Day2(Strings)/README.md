## Strings 
- python are surrounded by either single quotation marks, or double quotation marks.
- Example : 'hello' is the same as "hello".
- we can display a string literal with the print() function:

```python
print("Hello")
print('Hello')
```
--- 
### Slicing Strings
- You can return a range of characters by using the slice syntax.
- Specify the start index and the end index, separated by a colon, to return a part of the string.
- example: Get the characters from position 1 to position 5 (not included):

```python
b = "Hello, satish!"
print(b[1:5])
```
- Note: The first character has index 0.

----
### Slice From the Start: 
- By leaving out the start index, the range will start at the first character:
```python
txt = "Hello python learners"
print(txt[:5])
```
---

### Slice To the End
- By leaving out the end index, the range will go to the end:

```python
txt = "Hello python learners"
print(txt[12:])
```
---

### Negative Indexing
- Use negative indexes to start the slice from the end of the string:
```python
txt = "Hello python learners"
print(txt[-5:-2])
```
---
