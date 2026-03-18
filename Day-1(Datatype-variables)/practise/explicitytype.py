# Manually converts one data type into another using built-in functions like int(), float(), str(), complex(), etc.

# Example 1: Float → Int
x = 9.8
y = int(x)   # explicitly cast float to int
print(y)
print(type(y))

# Example 2: Int → Float
a = 7
b = float(a)   # explicitly cast into to float
print(b)
print(type(b))

# Example 3: Number → String
num = 123
s = str(num)   # convert int into string
print(s)
print(type(s))

# Example 4: String → Int
text = "56"
val = int(text)   # convert string into int
print(val + 10)
print(type(val))

# Example 5: String → Float
txt = "3.14"
pi = float(txt)    # convert string into float
print(pi * 2)
print(type(pi))

# Example 6: Int → Complex
n = 5
c = complex(n)     # convert int into complex
print(c)
print(type(c))

# Example 7: Boolean → Int
flag = True
num = int(flag)   # convert boolean into integer
print(num)
print(type(num))
