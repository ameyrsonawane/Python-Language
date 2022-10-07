# Dictionary is a collection of key and value pairs
# Dictionary is a mutable datatype
# Dictionary doesn't allow duplicates values

empty = {} # Empty Dictionary

int = {1:22,5:47,3:55}
print(int)
capital = {"Maharashtra":"Mumbai","Gujrat":"Gandhinagar","Rajsthan":"Jaipur"}
print(capital)

print(int[3])

# Adding items in Dictionary

capital["MP"]= "Bhopal"
print(capital)

int[77] = 99
print(int)

# Removing items from Dictionary

int.pop(5)
print(int)