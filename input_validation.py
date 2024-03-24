from math import sqrt

while True:
    number = float(input("Enter a number: "))
    if number == 0:
        print("Exiting...")
        break
    
    elif number > 0:
        print(sqrt(number))
    
    else:
        print("Invalid number")