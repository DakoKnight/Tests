story = ''
last_word = ''

while True:
    word = input("Please type in a word: ")

    if word == 'end' or last_word == word:
        break

    story = story + word + ' '
    last_word = word

print(story)