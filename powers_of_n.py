limmit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 0
result = 0

while limmit > result:
    result = base ** number
    number += 1
    if result <= limmit:
        print(result)