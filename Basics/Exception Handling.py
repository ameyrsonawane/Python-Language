try:
    x = int(input("Enter First Number:"))
    y = int(input("Enter Second Number:"))
    z = (x/y)
    print(z)
except Exception as s:
    print(s)


finally:  # Try with Finally
    print("No Exception")