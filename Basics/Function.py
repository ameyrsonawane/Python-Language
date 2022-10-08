# Function is a group of statements to performing a particular task.
# Builtin functions and user define functions these are the types of function
# Builtin functions - len(), print(), range(), zip()
# zip(*iterable) - It will map the values from list1 to list2


# zip(*iterable) --->

'''list1 = ["Maharashtra","Madhya Pradesh","Gujrat"]
list2 = ["Mumbai","Bhopal","Gandhinagar"]
s = zip(list1,list2)
print(list(s))

for l1,l2 in zip(list1,list2):
    print(l1,l2)


total_cost = [22,75,69,82]
sale_price =[15,85,55,95]
for x,y in zip(total_cost,sale_price):
    print("profit",x-y)'''
import multiplication as multiplication

# range(start,stop) --->

'''for x in range(1,10):
    print(x)'''


'''for y in range(1,10,3):
    print(y)'''


'''def addition(x,y):
    print(x+y)

addition(11,11)
addition(15,15)

def mul(a,b):
    print(a*b)

mul(5,2)
mul(9,5)'''

# Return -


def addition(x,y):
    return x+y
z = addition(25,25)
print(z)
m = z*2
print(m)
