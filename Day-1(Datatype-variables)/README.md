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
```python
Correct
a1 = 5;
_b2 = 10;
b = 10;

Incorrect
1a = 5;
23b = 10;
1@ = 5;

```

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

```python
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
print(b, "is complex number?", is instance(b, complex))

```
-----

# Scope of Variables
There are broadly two kinds of scopes in Python − 
- Global scope
- Local scope

# Global Scope :
A variable/name declared in the top-level segment (__main__) of a program is said to have a global scope and is usable inside the whole program (Can be accessed from anywhere in the program).

In Python, a variable declared outside a function is known as a global variable. This means that a global variable can be accessed from inside or outside of the function.

Example:

```python
x = "Global Variable"  # defined outside of the fucntion foo()
def foo(): 
    print("Value of x: ", x) 
foo()
```
Here, we created a global variable x = "Global Variable". Then, we created a function foo to print the value of the global variable from inside the function. 
We get the output : Global Variable

Thus we can conclude that we can access a global variable from inside any function.

What if you want to change the value of a Global Variable from inside a function?
```python
x = "Global Variable" 
def foo(): 
    x=x-1
    print("Value of x: ", x) 
foo()

In this code block, we tried to update the value of the global variable x. We get an output as:

UnboundLocalError: local variable 'x' referenced before assignment
```

This happens because, when the command x=x-1, is interpreted, Python treats this x as a local variable and we have not defined any local variable x inside the function foo().


# Local Scope:
The variables which are defined inside a function body have a local scope. This implies that local variables can be accessed only inside the function in which they are declared.

We declare a local variable inside a function. Consider the given function definition:

``` python
def func():
    name = "Satish Thapak"
    print(name)

func()
We get the output as: Satish Thapak
 
Accessing A Local Variable Outside The Scope

def func():
    name = "Satish Thapak"

func()
print(name)
 
In the above code, we declared a local variable y inside the function foo(), and then we tried to access it from outside the function. We get the output as:

NameError: name 'name' is not defined
```
We get an error because the lifetime of a local variable is the function it is defined in.

Outside the function, the variable does not exist and cannot be accessed. In other words, a variable cannot be accessed outside its scope.

---

## The Lifetime of a Variable
 
The time for which the variable exists in memory is called the lifetime of that variable:
- The lifetime of a Global variable is the entire program run (i.e., they live in the memory as long as the program is being executed).
- The lifetime of a Local variable is their function’s run (i.e., as long as their function is being executed).

Global Variable And Local Variable With The Same Name

Consider the code given:
``` python
val = 1 
def func():
  val = 50
  print("Value of Local variable:", val)
 
func() 
print("Value of Global Variable:", val)
```

In this, we have declared a global variable val = 1 outside the function func(). Now, we re-declared a local variable inside the function func() with the same name val. Now, we try to print the values of val, inside, and outside the function. We observe the following output:

```python
Value of Local variable:: 50
Value of Global variable:: 1
 ```
In the above code,  both global and local variables have the same name val. On printing the value of val we get a different result, because the variables have been declared in different scopes, i.e., the local scope inside func() and global scope outside func().

When we print the value of the variable inside func() it outputs Value of Local variable: 50. This is the local scope of the variable. In the local scope, it prints the value that it has been assigned inside the function.

Similarly, when we print the variable outside func(), it outputs Value of Global variable: 1. This is the global scope of the variable, and the value of the global variable val is printed.

---

## Typecasting
 
There may be times when you want to specify a type on to a variable. This can be done with type casting. Python is an OOP language, and as such, it uses classes to define data types, including its primitive types.

Type casting is the method to convert from data type to another data type, according to user's requirements. This article introduces to the different type of casting supported by Python and how to implement them.

Python supports two types of type casting –

Implicit Type Conversion
Explicit Type Conversion
 

# 1. Implicit Type Conversion:
 
In this, method, Python automatically converts one data type into another data type. There is no user intervention.
```python
val = 5
print(type(val))
 
output:

#Python automatically converts val to int.
< class 'int' >


Example:

a = 8.0
b = 4.0
m = a * b
print(m)
print(type(m))

output:

32.0
< class 'float' 
``` 

# 2. Explicit Type Conversion

In Explicit Type, the Conversion user needs to manually convert data types.

Mainly in typecasting can be done with these data type functions:

int() - int class to construct an integer literal.
float() - float class to construct a float literal.
str() - string class to construct a string literal.

Let’s see some examples of typecasting:

Example:
```python
# int variable
a = 5.9

# typecast to int 
n = int(a)
print(n)
print(type(n))
 

output:
5
<class 'int'>
```
 
Here, we are casting float into int data type with int() function.