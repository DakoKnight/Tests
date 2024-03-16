def isleapyear(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def nextleapyear(current_year):

    next_year = current_year + 1
    while True:
        if is_leap_year(next_year):
            return next_year
        next_year += 1

def main():
    try:
        current_year = int(input("Enter the current year: "))
        next_ly = next_leap_year(current_year)
        print(f"The next leap year after {current_year} is {next_ly}.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name == "__main":
    main()