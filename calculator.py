number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == 'add':
    result = number_1 + number_2
    print(number_1, '+', number_2, '=', result)

elif operation == 'multiply':
    result = number_1 * number_2
    print(number_1, '*', number_2, '=', result)
    
elif operation == 'subtract':
    result = number_1 - number_2
    print(number_1, '-', number_2, '=', result)