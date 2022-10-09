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
f.write("Wellcome Mr Amey into New Era")
f.close()

f = open("In.txt", "w")
l = [55, 87, 54, 28, 222]
for items in l:
    f.write(str(items))
f.close()


f = open("Sonawane.txt", "r")
print(f.read())
f.close()

