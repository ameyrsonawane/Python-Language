# Prime Number--> A number that can be divided exactly only by itself and 1.

'''num = int(input("Enter No:"))
for i in range(2,num):
    if num % i == 0:
        print("Not Prime No")
        break
else:
    print("Prime No")'''

# Palindrome Number--> A number that remains same when it's digits are reversed.(Ex- 525,242)

'''num = input("Enter input:")
reverse = num[-1::-1]
if (num == reverse):
    print("Palindrome")
else:
    print("Not Palindrome")'''


# Armstrong Number--> When the sum of nth power of each digit is equal to the number itself.

'''num = int(input("Enter No:"))
sum = 0
temp = num
n = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp//= 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''


# Fibonacci Series--> 0 1 1 2 3 5 8

'''num = int(input("Enter No:"))
x = 0
y = 1
z = 0
while z <= num:
    print(z)
    x = y
    y = z
    z = x+y'''


# Factorial-->  5 = 5*4*3*2*1 = 120

'''num = int(input("Enter No:"))
fac = 1
while(num > 0):
    fac = fac*num
    num = num-1
print("Factorial=",fac)'''


# Reverse String

'''s = (input("Enter name:"))
reverse = s[-1::-1]
print(reverse)'''

# Reverse String ( Using For Loop )

'''str = input("Enter String=")
for i in range((len(str)-1),-1,-1):
    print(str[i],end="")'''

# Reverse String (O/P - enawanoS ardnejaR yemA)

'''word = "Amey Rajendra Sonawane"
print(word)
word=word[-1::-1]
print(word)'''


# Reverse Words (I/P - Amey Sonawane   O/P - Sonawane Amey)

'''str="Amey Sonawane"
print(str[5:],str[:4])'''



# How to Swap any two number in List

'''l = [25,65,19,90,]
pos1 , pos2 = 1,3
l[pos1],l[pos2] = l[pos2],l[pos1]
print(l)'''


# Count the No. of occurrences in the string

'''s = input("Enter String-")
c = input("Enter Character to check the frequency-")
count = 0
for i in s:
    if i == c:
        count += 1
print(c,count)
       #break'''            # Number of occurrence O/P = 0



# Count the No. of occurrences in the string "of each character"

'''str = input("Enter Name=")
l=list(str)
f=[l.count(ele) for ele in l]
d=dict(zip(l,f))
print(d)'''


# How to find out count of Digits,Alphabets & Special Characters from string


'''str= "AMey#12345@"
count1=0
count2=0
count3=0
for i in str:
    if i.isdigit():
        count1=count1+1
    elif i.isalpha():
        count2=count2+1
    else:
        count3=count3+1

print("Digits=",count1)
print("Alphabets=",count2)
print("Special=",count3)'''




# How to Swap first and Last element in the list

'''l= ["Amey",1990,2022,"Sonawane",2023]
l[0],l[-1] = l[-1],l[0]
print("After Swapping -",l)'''


# How to find smallest and height numbers in list

'''l = [11,55,22,3,95,111]   # 1st Way 
l.sort()
print("Smallest No -",l[0])
print("Height No -",l[-1])'''

'''print("Smallest No -",min(l))    # 2nd WAy
print("Height No -",max(l))'''


# Sum of digit in the string

'''a ="02222225"
sum = 0
for x in a:
    if x.isdigit():
        sum = sum + int(x)
print(sum)'''


# Sum of digit in the string - (Take the input from Keyboard)

'''str = input("Enter string-")
sum = 0
for i in range(0,len(str)):
    if (str[i].isdigit()):
        sum = sum+int(str[i])
print(sum)'''


# How to Search element in the list

'''l = ["Amey",1,55,"Sonawane",222]   # 1st Way
print("Ame" in l)'''


'''l = [1,22,55,78]                     # 2nd Way
num = int(input("Enter No="))
for i in l:
    if i == num:
        print("Present")
        break
else:
 print("Not Present")'''

'''l = [11,22,44,87,98]
#c = list(l)
print(l)'''


# How to reverse list

'''l = [44,78,25,85,77]
r = l[-1::-1]
print(r)'''


# Reverse List Like-->   I/P=[1,2,3,4,5,6]   O/P=[3,2,1,6,5,4]

'''l=[1,2,3,4,5,6]
print(l)
l[0],l[2]=l[2],l[0]
l[3],l[-1]=l[-1],l[3]
print(l)'''


# Find out the pairs from List who sum = 12


'''l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==12:
            print(l[i],l[j])'''


# Pyramid Shape

'''num = int(input("Enter Number of Rows-"))
for i in range(0,num):         # (for loop)-for rows
    for j in range(0,num-i-1): # (for loop)-for columns and print space
        print(" ",end="")      # print space and end="" parameter keep on the same line
    for j in range(0,i+1):     # (for loop)-for columns and print star
        print("*",end=" ")     # print star
    print()      '''              # print function for new line


# Pyramid shape --->                                          #     1
                                                              #    1  2
'''num = int(input("Enter the number of rows="))              #   1  2  3
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
     print(j+1,end=" ")
    print()'''

# Pyramid shape --->                                        #       1
                                                            #      2  2
'''num = int(input("Enter the number of rows="))            #     3  3  3
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
     print(i+1,end=" ")
    print()'''


# Lambda Function --->

'''square = lambda x: x*x
print(square(6))'''


'''sum = lambda a,b,c: a+b+c
print(sum(80,3,1))'''


# Update value with another value in Dictionary

'''d={"Amey":1995,"Nishtha":2020}
print(d)
d["Amey"]=1990
print(d)'''


# Swapping

'''a=5
b=8
print("a =",a)
print("b =",b)
a=a^b
b=a^b
a=a^b
print("a =",a)
print("b =",b)
'''

# Swapping (Using another variable)

'''a=5
b=8
print("a =",a)
print("b =",b)
temp = a
a=b
b = temp
print("a =",a)
print("b =",b)
'''

# Try: and Except:

'''try:
    num= "a"
    if num%2==0:
        print("Even Number")
    else:
        print("Number is not even")
except:
    print("Please Enter only Number")'''



#  Remove Extra Space from the string along with ? ! .


'''str= input("Enter String=")
s= ""
for i in range(len(str)):
    if str[i]==" " and str[i+1]==" ":      # (string without "? ! .")


    #if str[i]==" " and (str[i+1]==" " or str[i+1]=="?" or str[i+1]=="!" or str[i+1]=="."):
        continue
    else:
        s=s+str[i]
print(s)'''


# Print the digits only from string


'''str="test123$"
for i in str:
    if i.isdigit():
        print(i)'''



# Generator ==>  Generator will give you iterator(Ex- We want to fetch 1000 records from DB to print/process.
# So here all 1000 records will be loaded in your memory, we don't want it.
# We want work on one value at a time in this case we have to use generator. we use yield)

# program for find-out the square.


'''def topten():
    num=1
    while num<=10:
        sq= num * num
        yield sq
        num+=1
values= topten()    #  --> (Create the object to call method)
for i in values:
    print(i)'''



#  Deep Copy and Shallow Copy


# Deep Copy==> In deep copy, when we do any changes in copy of the object it will not reflect in the original object.

'''import copy                     #(By Default Installed)
l=[[1,2],[3,4]]
cp=copy.deepcopy(l)
print(cp)
cp[0][0]=45
print("Copy of Object=",cp)
print("Original Object=",l)'''    # (To check the changes will reflect or not in the original object )



# Shallow Copy==> In shallow copy, when we do any changes in copy of the object it will reflect in the original object.


'''import copy                     #(By Default Installed)
l=[[1,2],[3,4]]
sh=copy.copy(l)
print(sh)
sh[0][0]=55
print("Copy of Object=",sh)
print("Original Object=",l)'''    # (To check the changes will reflect or not in the original object )

# Shallow copy behave like Deep copy for simple list ?.

# ==>


# Multiple Inheritance

'''
class movie:
    def d1 (self):
        print("Base Class")
class actor(movie):
    def d2 (self):
        print("1st Derived Class")
class director(actor):
    def d3 (self):
        print("2nd Derived Class")
obj=director()
obj.d1()
obj.d2()
obj.d3()
'''