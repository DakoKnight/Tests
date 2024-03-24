name = input("Please tell me your name: ")

if name.lower() == 'jerry':
    print("Next please!")

else:
    portions = int(input("How many portions of soup? "))
    total = portions * 5.90
    print("The total cost is", total)
    print("Next please!")
