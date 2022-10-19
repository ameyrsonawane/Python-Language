# Prime Number--> A number that can be divided exactly only by itself and 1.

'''num = int(input("Enter No:"))
for i in range(2,num):
    if num % i == 0:
        print("Not Prime No")
        break
else:
    print("Prime No")'''

# Palindrome Number--> A number that remains same when it's digits are reversed.(Ex- 525,242)

'''num = (input("Enter input:"))
reverse = num[::-1]
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
    print("Armstrong No")
else:
    print("Not Armstrong No")'''


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
reverse = s[::-1]
print(reverse)'''


# How to Swap any two number in List

'''l = [25,65,19,90,]
pos1 , pos2 = 1,3
l[pos1],l[pos2] = l[pos2],l[pos1]
print(l)'''


# Count the No. of occurrences in the list

'''s = input("Enter String")
c = input("Enter Character to check the frequency ")
count = 0
for i in s:
    if i == c:
        count += 1
print(c,count)'''

# How to Sum, Multiplication and Division of all numbers in the list (Error)


'''size = int(input("Enter Numers"))
for i in range(size):
    val = int(input("Enter Number"))
    size.append()
    sum = 0
    for i in range(size):
        sum = sum = size[i]
        print(sum)'''


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


# Sum of digit in the string (Check O/P)

'''a = '02222225'
sum = 0
for x in a:
    if x in digit():
        sum = sum + int(x)
        print(sum)'''


# How to Search element in the list

'''l = ["Amey",1,55,"Sonawane",222]   # 1st Way
print("Ame" in l)'''


'''l = [1,22,55,78]                     # 2nd Way
num = int(input("Enter No"))
for i in l:
    if i == num:
        print("p")
        break
else:
 print("A")'''

'''l = [11,22,44,87,98]
#c = list(l)
print(l)'''


# How to reverse list

'''l = [44,78,25,85,77]
r = l[-1::-1]
print(r)'''

# Pyramid Shape

'''num = int(input("Enter Number"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end="")
        print()'''


'''def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'*'*(2*i+1))'''

