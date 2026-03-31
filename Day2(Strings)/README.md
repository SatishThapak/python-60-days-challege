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

### Modify Strings
- Python has a set of built-in methods that you can use on strings.

1. ### Upper Case
- The upper() method returns the string in upper case:
```python
txt = "Hello python learners"
print(txt.upper())
```
2. ### Lower Case
- The lower() method returns the string in lower case:
```python
txt = "Hello python learners"
print(txt.lower())
```
3. ### Remove Whitespace
- The strip() method removes any whitespace from the beginning or the end:
```python
txt = "  Hello python learners "
print(txt.strip())
```
4. ### Replace String
- The replace() method replaces a string with another string:

```python
txt = "Hello python learners"
print(txt.replace("H", "c"))
```
5. ### Split String
- The split() method returns a list where the text between the specified separator becomes the list items.

```python
txt = "Hello python learners"
print(txt.replace("H", "c"))
```
6. ### String Concatenation
- To concatenate, or combine, two strings you can use the + operator.

```python
txt = "Hello python"
txt1 = "learners"
text = txt+txt1
print(text)
```
- To add a space between them, add a " ":

```python
txt = "Hello python"
txt1 = "learners"
text = txt+" " + txt1
print(text)
```
7. ### Format - Strings
- We cannot combine strings and numbers like this:
```python
age = 35
#This will produce an error:
txt = "My name is Satish, I am " + age
print(txt) 
```
- But we can combine strings and numbers by using f-strings or the format() method!
```python
age = 35
#This will produce an error:
txt = "My name is Satish, I am " + age
print(txt) 
```
### F-Strings
- F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
- To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

- Create an f-string:
```python
age = 36
txt = f"My name is Satish, I am {age}"
print(txt)
```
---

## Placeholders and Modifiers
- A placeholder can contain variables, operations, functions, and modifiers to format the value.

- Example: 
Add a placeholder for the age variable:
```python
age = 35
txt = f"I am {age} years old"
print(txt)
```
- A placeholder can include a modifier to format the value.
- A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

```python
age = 35.06
my_age = f"I am {age:.2f} years old"
print(my_age)
```
- A placeholder can contain Python code, like math operations:
- Perform a math operation in the placeholder, and return the result:

```python
age = f"I am {5*7} years old"
print(age)
```
--- 

## String Methods
- Python has a set of built-in methods that you can use on strings.
### Note: All string methods return new values. They do not change the original string.
- Examples: capitalize(),casefold(),count() etc. there are many built-in methods.

