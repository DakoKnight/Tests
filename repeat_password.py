entry = input("Enter password: ")

while True:
    password = input("Repeat password: ")
    if password == entry:
        print("User account created!")
        break

    else:
        print("They do not match!")