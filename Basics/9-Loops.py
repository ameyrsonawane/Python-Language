# While Loop -->

# Use to iterate block of code as long as test expression is true.
# Firstly test expression is checked if it is evaluated to true then body of the loop will evaluate
# Conditions are used to stop the loop
# Can iterate on list,string,tuple,dictionary

# while test expression:
#        body of while loop

x = 0
while x <= 10:
    print(x)
    x = x+1
print("Out of while loop")


name = "Amey"
x = 0
while x < len(name):
     print(name[x])
     x = x+1


# For Loop -->

city = [["Jalgaon","Pune"],["Dhule","Pune"],["Nashik","Pune"]]
for c in city:
    print(c)

# Convert List into Dictionary

dictionary = dict(city)
print(dictionary)
for city in dictionary:
    print(city)

for city, address in dictionary.items(): # print keys and values of the dictionary
    print(city, address)





# Break and Continue Statement ->

# Break statement instruct the programme to exit from the current loop.
# Continue statement instruct the programme to skip the current iteration and continue with next one.
# Paas statement instruct the programme to do nothing.












