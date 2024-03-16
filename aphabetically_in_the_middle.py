letter1 = input("Enter the first letter: ")
letter2 = input("Enter the second letter: ")
letter3 = input("Enter the third letter: ")

if letter2 < letter1 < letter3 or letter3 < letter1 < letter2:
    print("The letter in the middle is ", letter1)

elif letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print("The letter in the middle is ", letter2)

elif letter2 < letter3 < letter1 or letter1 < letter3 < letter2:
    print("The letter in the middle is ", letter3)