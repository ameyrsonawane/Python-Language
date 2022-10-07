# Set is an unordered collection with no duplicate elements
# set is used for to remove the duplicate values.
# Set is a mutable datatype
# Set support mathematical operation


'''sets = {10,30,50,90,30} # Set doesn't have specific order
print(sets)
print(50 in sets) # Membership Operator
print("50" in sets)'''


# Set Methods --->


# 1) add(element) -> Add element to the set

country = {"India","Russia","Nepal"} # Set-1
state = {"Maharashtra","Gujrat","Himachal","Gurgaon"} # Set-2


print(country)
country.add("Africa")
print(country)

# 2) remove(element) -> Remove the element from set

country.remove("Nepal") # discard
print(country)

# 3) pop() -> Remove the element from set(Last element)

country.pop()
print(country) # Set doesn't follow order and pop() remove the last element


# 4) union()

world = country.union(state)
print(world)

# 5) clear() -> Remove all elements from the set

country.clear()
print(country)




