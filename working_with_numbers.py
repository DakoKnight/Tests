count = 0
sum = 0
mean = 0
pos_count = 0
neg_count = 0

print("Please type in interger numbers. Type in 0 to finish")

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    elif number > 0:
        pos_count += 1
    else:
        neg_count += 1
    sum += number
    count += 1

mean = sum / (count - 1)

print("Numbers typed in ", count)
print("The sum of the numbers is ", sum)
print("The sum of the numbers is ", mean)
print("Positive number ", pos_count)
print("Negative number ", neg_count)