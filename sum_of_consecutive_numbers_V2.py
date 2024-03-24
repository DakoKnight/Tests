limit = int(input("Limit: "))

sum = 0
output = ""
number = 1

while sum < limit:
    sum += number
    output += str(number)
    if sum < limit:
        output += ' + '
    number += 1
        
print(f"The consecutive sum: {output} = {sum}")