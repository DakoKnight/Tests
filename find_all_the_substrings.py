#word = input("Please type in a word: ")
word = "incomprehensibilities"
#char = input("Please type in a character: ")
char = 'i'

result = ''
index = 0

while index < len(word) and char in word:
    # Find the index of the char and stores it
    index = word.find(char)
    i = index   # Counter equal to index
    # Loop to print the char and the two next chars
    while i < index + 3:
        result += word[i]
        i += 1
    
    print(result)
    result = ''
    word = word[index + 1:]
    i = 0
