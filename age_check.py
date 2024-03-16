age = int(input('What is your age: '))

if 0 < age > 5:
    print("Ok, you're", age, "years old")

elif age < 1:
    print('This must be a mistake')

else:
    print("I suspect you can't write quite yet...")