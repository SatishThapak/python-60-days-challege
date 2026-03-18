# Manually converts one data type into another using built-in functions like int(), float(), str(), complex(), etc.

# Example 1: Float → Int
x = 9.8
y = int(x)   # explicitly cast float to int
print(y)
print(type(y))

# Example 2: Int → Float
a = 7
b = float(a)   # convert int to float
print(b)
print(type(b))

# Example 3: Number → String
num = 123
s = str(num)   # convert int to string
print(s)
print(type(s))

# Example 4: String → Int
text = "56"
val = int(text)   # convert string to int
print(val + 10)
print(type(val))

# Example 5: String → Float
txt = "3.14"
pi = float(txt)
print(pi * 2)
print(type(pi))

# Example 6: Int → Complex
n = 5
c = complex(n)
print(c)
print(type(c))

# Example 7: Boolean → Int
flag = True
num = int(flag)
print(num)
print(type(num))
