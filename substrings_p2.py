string = input("Please type in a string: ")

i = len(string) - 1

while i >= 0:
    print(string[i:len(string)])
    i = i - 1
