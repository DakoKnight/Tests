wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

if day.lower() == 'sunday':
    wage = wage * 2

print("Daily wages:", wage * hours, "euros")