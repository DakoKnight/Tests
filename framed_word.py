word = input("Word: ")

frame = '*'
blank1 = ''
n = 0
i = 1

if len(word) % 2 == 0:
    n = (28 - len(word)) / 2
    while i <= n:
        blank1 += ' '
        i += 1
    blank2 = blank1

else:
    n = int(28 - len(word)) / 2
    while i <= n:
        blank1 += ' '
        i += 1
    blank2 = blank1 + ' '

print('******************************')
print('*' + blank1 + word + blank2 + '*')
print('******************************')