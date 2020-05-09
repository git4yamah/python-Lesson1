# A function can have zero, one or multiple parameter and still execute the function. See examples below:

# Zero parameter:

def f():
    return 5*5
r = f()
print (r)

# one parameter:

def f(x):
    return x + 100
p = f(200)
print (p)

# multiple parameter:

def f(x,y,z):
    return x + y + z
q = f(1,2,3)
print (q)
