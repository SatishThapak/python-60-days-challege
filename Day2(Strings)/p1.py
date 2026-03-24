def f1():
    global x
    x+=1
    print(x)

x=12
f1()    
print("x")

'''
Execution flow:
x = 12 → A global variable x is created with value 12.

f1() is called:

Inside f1(), global x tells Python to use the global variable x.

x += 1 increments x from 12 to 13.

print(x) prints 13.

After the function call, print("x") prints the literal string "x", not the variable.

'''



# example
def fun():
    x=15
    print(x)

x=12
fun()

''' Execution flow:
x = 12 → A global variable x is created with value 12.

fun() is called:
  Inside fun(), a new local variable x is created with value 15.
  print(x) prints the local x, which is 15.After the function finishes,
  the global x is still 12 because the local x inside the function does not affect the global one.
'''

