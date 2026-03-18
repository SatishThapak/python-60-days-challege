# Add Two Numbers with User Input
# input() always returns a string, no matter what you type.
x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)    # explicitly cast both inputs to int

print("The sum is: ", sum)
print(type(sum))


# we can also write like this as well:  
# The result will be a string because input() always returns text.

x = input("Type a number: ") 
y = input("Type another number: ")

sum = x + y   # concatenates strings, not numbers

print("The sum is: ", sum)
print(type(sum))

