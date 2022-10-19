# Datatypes in Python --> 1) Integer 2) Floating Numbers 3) String 4) Boolean values 5) Tuple 6) Array 7) Dictionary

# String-Sting is a datatype, it's sequence of characters enclosed in quotes. (always start from 0 index)
# For single line string we use ' ' / " "
# For multiline string we use '''  ''' / """  """


'''x = "Welcome into the Object Oriented Language-Python"
y = 'Learn all those things which are available in this language'
print(x)
print(y)
print(x[1]) # to display particular character'''

'''x = "Please do 'practice' on daily basis to learn me"
y = 'Otherwise it will be "difficult" to understand what exactly I am'
print(x)
print(y)'''

'''z = """This is the multiline 
sting"""
print(z)
print("is" in z) # Membership Operator
print("it's" in z) # Membership Operator'''


# String Functions ----->


# 1) len(s)- Return number of characters

s = ("Amey")
print(len(s))

# 2) str(s)- Convert specified values into a string

x = 114477
print(str(x))

# 3) upper(s)- Convert a string into upper case

s="Amey"
print(s.upper())

# 4) Count(s)- Return the number of times a specified value is found

s="Amey,Amey,Amey,AMEY"
print(s.count("Amey"))
print(s.count("Amey",5,15))

# 5) string_endwith(s)-

#s = "Amey"
#print(s.string_endwith())

# 6) String find(s)

#s = "Amey"
#print(s.find[2])

# 7) String replace(s)

s = "Amey"
print(s.replace("Amey","Sonawane"))

# 8) String split()

s = "Amey Rajendra Sonawane"
print(s.split())

# 9) Strip()
s = "Amey Sonawane"
print(s.strip())


# String Slicing --->

# s[i:j] - Slice of s from i to j
# s[i:j:k]- Slice of s from i to j with step k
# s[start-index:end-index:step]

'''s = "Amey Rajendra Sonawane"
print(s[0])
print(s[1])
print(s[-1])
print(s[-3])
print(s[0:9])
print(s[1:3])
print(s[0:])
print(s[:4])
print(s[-8:-5])

print(s[::-1]) # Reverse String'''


# String Formatting --->



