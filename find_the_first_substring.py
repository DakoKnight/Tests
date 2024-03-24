word = input("Please type in a word: ")
char = input("Please type in a character: ")

result = ''
index = word.find(char)
i = index

if char in word:
    if (len(word) - 1) - index > 2:
        while index < i + 3:
            result += word[index]
            index += 1

        print(result)