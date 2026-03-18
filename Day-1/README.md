# Introduction to Variables

Variables are labels/names to which we can assign value and use them as a reference to that value throughout the code.

## Variables are fundamental to programming for two reasons:
1. Variables keep values accessible
2. Variables give values context

---

## How are Values Assigned to A Variable?

For Example:
```python
Student = "Jacob"
Age = "19"
```
---
# Python will internally create labels referring to these values as shown below:
![variables](../images/variables.png)

## Naming a Variable
You must keep the following points in your mind while naming a variable:

- Variable names can contain letters, numbers, and underscores.
- They cannot contain spaces.
- Variable names cannot start with a number.
- Variable names are case-sensitive.
For example: The variable names Temp and temp are different.

While writing a program, creating self-explanatory variable names helps a lot in increasing the readability of the code. However, too-long names can clutter up the program and make it difficult to read.

Examples:
Correct
a1 = 5;
_b2 = 10;
b = 10;

Incorrect
1a = 5;
23b = 10;
1@ = 5;



## Data Types
In Python, data types define the kind of data a variable can hold.
Python has a dynamic data type system, meaning you don’t need to declare the type explicitly — it is determined at runtime.

## Built-in Data Types:
- Numbers
- Integers
- Floating Point Numbers
- Complex Numbers
- Strings
- Boolean Values
- List, Tuple, and Dictionary

Examples:
a = "Raw"    # String Data Type
a = 10       # Integer Data Type
a = 5.6      # Floating Point Number Data Type
a = 1+8j     # Complex Number
a = True     # Boolean Value

# Checking Data Types
b = 5
print(b, "is of type", type(b))

b = 2.0
print(b, "is of type", type(b))

b = 1+2j
print(b, "is complex number?", isinstance(b, complex))
