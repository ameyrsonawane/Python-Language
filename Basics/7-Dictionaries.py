# Dictionary is a collection of key and value pairs
# Dictionary is a mutable datatype
# Dictionary doesn't allow duplicates values
# Dictionary is unordered


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


# Dictionary Methods --->


city = {"Dhule":"Deopur","Jalgaon":"Aadarshnagar","Pune":"Wagholi"}

print(city)


# 1) get() - Return the value for specified key in the dictionary

print(city.get("Pune"))

# 2) keys() - Return the copy of dictionary's keys

print(city.keys())

# 3) items() - Return the copy for dictionary key-value pair

print(city.items())

# 4) values() - Return the copy of values in the dictionary

print(city.values())

# 5) pop() - Remove the item with specified key

print(city.pop("Dhule"))

# 6) popitem() - Remove the key value pair

print(city.popitem())

# 7) update() - Add the specified key value pair to dictionary

city.update({"Mumbai":"Bandra"})
print(city)

# 8) copy() - Return the copy of dictionary

c = city.copy()
print(c)


# 9) clear() - Remove the elements from dictionary

print(city.clear())


