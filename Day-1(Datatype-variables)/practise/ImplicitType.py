# This happens when Python automatically promotes one data type to another to avoid data loss during operations.

# Example 1: Integer + Float

x = 10      # int
y = 2.5     # float
z = x + y
print(z)
print(type(z))

# Example 2: Integer + Complex

a = 5       # int
b = 3j      # complex
c = a + b
print(c)
print(type(c))

# Example 3: Boolean in Arithmetic
val = True   # bool  # 
num = 10     # int
result = val + num
print(result)
print(type(result))

# Example 4: Division Always Returns Float
p = 7
q = 2
result = p / q
print(result)
print(type(result))

# Example 5: Mixed Types in Expressions

x = 2       # int
y = 3.0     # float
z = 4j      # complex
result = x + y + z
print(result)
print(type(result))

