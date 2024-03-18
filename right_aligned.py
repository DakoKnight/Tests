i = 1

string = input("Please type in a string: ")
count = 20 - len(string)
print(len(string))

output = ""


while i <= count:
    i += 1
    output += '*'
 
print(output + string )