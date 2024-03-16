year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("The year is a leap year.")
    else:
        print("That year is not a leap year.")

elif year % 4 == 0:
    print("The year is a leap year.")

else:
    print("That year is not a leap year.")