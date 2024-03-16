gift_value = float(input("Value of gift: "))

if 5000 <= gift_value < 25000:
    taxes = 100 + (gift_value - 5000) * 0.08
    print(str(taxes))

elif 25000 <= gift_value < 55000:
    taxes = 1700 + (gift_value - 25000) * 0.1
    print(str(taxes))

elif 55000 <= gift_value < 200000:
    taxes = 4700 + (gift_value - 55000) * 0.12
    print(str(taxes))

elif 200000 <= gift_value < 1000000:
    taxes = 22100 + (gift_value - 200000) * 0.15
    print(str(taxes))

elif gift_value >= 1000000:
    taxes = 142100 + (gift_value - 1000000) * 0.17
    print(str(taxes))

else:
    print("No tax!")