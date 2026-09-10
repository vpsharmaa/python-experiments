from datetime import date

def find_day(d, m, y):
    given_date = date(y, m, d)   # Note: year, month, day order
    return given_date.strftime("%A")   # %A gives full weekday name

# Taking input from user
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

print("The day of the week is:", find_day(d, m, y))
