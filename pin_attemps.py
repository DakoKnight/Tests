pin = "4321"
attempts = 0

while True:
    entry = input("PIN: ")
    if entry == pin and attempts == 0:
        print("Correct! It only took you one single attempt")
        break
    
    elif entry == pin and attempts != 0:
        attempts += 1
        print("Correct! It took you ", str(attempts), "attempts")
        break

    else:
        attempts += 1
        print("Wrong!")


