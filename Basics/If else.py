x = 22
y = 11

if x == y:
    print("equal")
else:
    print("not equal")


if x > y:
    print("True")
else:
    print("False")


if x > y and x == y: # Both conditions should be satisfied
    print("Satisfied")
else:
    print("Not Satisfied")


if x > y or x == y: # Any one condition should be satisfied
    print("Satsfied")
else:
    print("Not Satisfied")


score = 95
if score>90:
    print("1st Rank")
elif score > 35:
    print("Pass")
else:
    print("Failed")


