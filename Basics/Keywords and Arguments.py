# Keywords and Positional Arguments --->

# 1) Positional Arguments
# 2) Keyword Arguments
# 3) Required Arguments
# 4) Optional Arguments

def add(x,y): # When we define a function x and y is known as parameter
    return x + y
z = add (25,35) # When we call this function and provide a values of x and y (25,35)is known as arguments - (Positional Arguments)
print(z)

def add(x=20,y=2):
    return x + y
z = add()
print(z)


print(add(25)) # Value is assign to x - (Optional Arguments)

print(add(8,2)) # Values are assign to x and y - (Optional Arguments)

print(add(y=25)) # We can specify the values to parameter using keywords - (Keyword Arguments)

print(add(y=25,x=5)) # We can specify the values to parameter using keywords - (Keyword Arguments)


