while True:
    weight = float(input("Please enter your weight: "))
    unit = input("Kg(K) or lbs(L)? ")

    if unit.lower() == 'l':
        weight = weight / 2.2
        print(round(weight, 2), 'Kg')

    elif unit.lower() == 'k':
        weight = weight * 2.2
        print(round(weight, 2), 'lbs')
    
    else:
        print("Invalid entry!")