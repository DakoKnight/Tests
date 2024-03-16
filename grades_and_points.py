points = int(input("How many points [0-100]: "))

if 0 <= points <= 49:
    print('fail')

elif 50 <= points <= 59:
    print('1')

elif 60 <= points <= 69:
    print('2')

elif 70 <= points <= 79:
    print('3')

elif 80 <= points <= 89:
    print('4')

elif 90 <= points <= 100:
    print('5')

else:
    print("impossible!")