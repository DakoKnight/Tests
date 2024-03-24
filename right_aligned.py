string = input("Please type in a string: ")
count = 20 - len(string)

i = 1
output = ""

while i <= count:
    i += 1
    output += '*'
 
print(output + string )