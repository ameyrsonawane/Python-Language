# Tuple is an immutable datatype
# It's represent with parentheses
# Tuple required single block to store the data
# Tuple allow duplicate values

tuple1 = (1,2,3,4,5,5,5) # Start from 0 index
tuple2 = ("India","Maharashtra","Pune","Wagholi")
tuple3 = (22,"Amey",True,True,45.99)


print(tuple2[1])

print(tuple1.count(5))

print(tuple3.count(True))

print(tuple2.index("Pune"))

for address in tuple2:
    print(address)


join_tuple = tuple1 + tuple2 + tuple3

print(join_tuple)

print(type(join_tuple))

print(tuple2[0:2])

print(tuple1[-1])


