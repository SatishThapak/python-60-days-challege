# Python Syntax
print("Hello, World!")

# Python Indentation
# Python uses indentation to indicate a block of code.

if 5 > 2:
  print("Five is greater than two!")  # Indentation refers to the spaces at the beginning of a code line.

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# Python will give you an error if you skip the indentation:
#if 5 > 2:
#print("Five is greater than two!")

# Checking Data Types
b = 5
print(b, "is of type", type(b))

b = 2.0
print(b, "is of type", type(b))

b = 1+2j
print(b, "is complex number?", isinstance(b, complex))

b = (True)
print(b,"is of type",type(b))

a = "123" 
print(a,"is of type",type(a))