temp = float(input("Please type in a temperature (F): "))

c = (temp - 32) * 5 / 9

print(temp, "degrees Fahrenheit equals", c, "degrees Celsius")

if c < 0:
    print("Brr! It's cold in here!")