import datetime


today = datetime.datetime.today()
print("Today's date and time",today)

today = datetime.datetime.today().date()
print("Today's date is",today)

today = datetime.datetime.today().time()
print("Current time is",today)