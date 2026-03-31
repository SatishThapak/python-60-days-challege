## Lists in Python
- Lists are used to store multiple items in a single variable.
- They are one of 4 built-in data types in Python for collections:
**List**      : ordered, mutable, allows duplicates.
**Tuple**     : ordered, immutable.
**Set**       : unordered, no duplicates.
**Dictionary**: key-value pairs.

- Lists are created using square brackets [].*

### Example
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing items
print(fruits[0])   # apple

# Modifying items
fruits[1] = "orange"
print(fruits)      # ['apple', 'orange', 'cherry']

# Adding items
fruits.append("grape")
print(fruits)      # ['apple', 'orange', 'cherry', 'grape']

# Removing items
fruits.remove("apple")
print(fruits)      # ['orange', 'cherry', 'grape']
```

### The list() constructor in Python is another way to create lists, besides using square brackets []. It can take any iterable (like strings, tuples, sets, or other lists) and convert it into a list.

# Examples
1. Empty list
```python
my_list = list()
print(my_list)   # []
```
2. From a string
```python
my_list = list("hello")
print(my_list)   # ['h', 'e', 'l', 'l', 'o']
```
3. From a tuple
```python
my_list = list((1, 2, 3))
print(my_list)   # [1, 2, 3]
```
4. From a set
```python
my_list = list({10, 20, 30})
print(my_list)   # [10, 20, 30]  # order may vary
```
5. From a dictionary
```python
my_list = list({"a": 1, "b": 2})
print(my_list)   # ['a', 'b']  # only keys are taken
```
