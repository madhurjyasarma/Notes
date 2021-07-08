
year = int(input("Enter a year: "))
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year,"is a leap year")
    elif year % 400 == 0:
        print("it's a leap year")
    else:
        print(False)

is_leap(year)
