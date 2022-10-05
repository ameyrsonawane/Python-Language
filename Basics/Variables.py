# Variables is a container which is used to store the value.
# Rules for defining the variables-
# 1- Variable contain alphabets, digit and underscore
# 2- It should start with alphabets and underscore
# 3- Space doesn't allow
# 4- Variable is a case-sensitive
# 5- We can't use reserved keywords for naming a variable


username="Welcome"   # username is a variable.
print(username)
print(type(username))  # type() is used to find out datatype of given variables.


x=600
print(x)
x=800
print(x)


x=600
print(x)
y=x
print(y)

print(id(x))
print(id(y))