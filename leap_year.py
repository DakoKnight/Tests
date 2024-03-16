year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100:
    if year % 400:
        print("The year is a leap year.")

elif year % 4:
    print("The year is a leap year.")

else:
    print("That year is not a leap year.")