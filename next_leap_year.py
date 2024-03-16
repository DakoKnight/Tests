year = int(input("Enter a year: "))
leap_year = year

while True:
    if leap_year == year:
        leap_year += 1
    elif leap_year % 4 == 0 and leap_year % 100 == 0:
        if leap_year % 400 == 0:
            break
        leap_year += 1
    elif leap_year % 4 == 0:
        break
    else:
        leap_year += 1

print("The next leap year after", year, " is ", leap_year)
