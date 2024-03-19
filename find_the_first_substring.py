word = input("Please type in a word: ")
char = input("Please type in a character: ")

result = ''

if char in word:
    index = word.find(char)
    i = index
    while index < i + 3:
        result += word[index]
        index += 1

    print(result)

else:
    pass