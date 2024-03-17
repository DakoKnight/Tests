limit = int(input("Limit: "))

sum = 0
number = 0
output = ""

while limit > sum:
    number += 1
    if sum != limit:
        output += str(number)
        sum += number
        if sum + number >= limit:
            break
        output += " + "
    
print("The consecutive sum:", output, "=", sum)