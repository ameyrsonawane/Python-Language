# Manual Steps to write the files -->

# 1) Open notepad and create file
# 2) Write in the file
# 3) close the file

# Mode

# Read mode: r
# Write mode: w
# Append mode: a
# Read/Write: r+


f = open("Sonawane.txt", "w")
f.write("Wellcome Mr Amey into New Era.")
f.close()

f = open("In.txt", "w")
l = [55, 87, 54, 28, 222]
for items in l:
    f.write(str(items))
f.close()


f = open("Sonawane.txt", "r")
print(f.read())
f.close()

f = open("Sonawane.txt","r+")
f.write("We are very happy to see you here.")
f.close()

'''f = open("Sonawane.txt", "r+")
print(f.read())
f.close()'''

f = open("Sonawane.txt","a")
f.write(" Thank you!")
f.close()

f = open ("Sonawane.txt","r")
print(f.read())
f.close()


# With keyword(No need to close the files)

with open("int.txt","w") as fw:
    fw.write("Using with keyword, no need to close the file")

with open("int.txt","r") as fr:
    print(fr.read())



