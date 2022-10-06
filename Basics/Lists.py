# List is mutable datatype, it's represent with square bracket. (List start from 0 index)
# List has large memory, because list store in 2 blocks memory,
# one is fixed size and another is variable size to store the data.
# List allow duplicate values, list have multiple datatype
# List store the value based on index, so we can add,remove the items from list.


'''a = [10,40,90] # (List start from 0 index)
b = ["Amey","Rajendra","Sonawane"]
c = [10,"20",40,"sir",50.1]

print (a[2])
print(type(c))
print(type(b))
print(c[0:4])
print(c[4])
print(c[0:4:2])'''


# List Methods --->


# 1) list.append(i,x) -> Add an item to end of the list

cities = ["Dhule","Pune","Jalgaon"]
print(cities)
cities.append("Nagpur")
print(cities)

# 2) list.insert(i,x) -> Insert an item at a given position
names = ["Amar","Nikhil","Pooja","Payal" ]
print(names)
names.insert(3,"Sachin")
print(names)

# 3) list.remove(x) -> Remove the first item from the list whose value is equal to x

state = ["Maharashtra","Gujrat","Delhi","Maharashtra","Himachal"]
print(state)
state.remove("Maharashtra")
print(state)

# 4) list.pop(i) -> Remove the item at the given position in the list, and return it. If no index is specified,
# a.pop() remove and returns the last item in the list.

country = ["India","Srilanka","Nepal","Russia"]
print(country)
country.pop(2)
print(country)

# 5) list.count(x) -> Return the number of times x appears in the list

car = ["Nexon","City","i20","Nexon","Safari","XUV700","Nexon"]
print(car.count("Nexon"))


# 6) list.sort(*,key=None,reserve=false) -> Sort the items of the list in place.

IT = ["Infosys","L&T","HCL","Mphasis"]
print(IT)
IT.sort()
print(IT)

# 7) list.reverse() -> Reverse the element of the list

laptop = ["Sony","Dell","HP","Acer"]
print(laptop)
laptop.reverse()
print(laptop)

# 8) list.clear() -> Remove all items from the list

mobile = ["Apple","Redmi","Vivo","Oppo"]
print(mobile)
mobile.clear()
print(mobile)

