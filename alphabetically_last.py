first_word = input('Please type in the 1st word: ')
second_word = input('Please type in the 2nd word: ')

if first_word > second_word:
    print(first_word, 'comes alphabetically last.')

elif second_word > first_word:
    print(second_word, 'comes alphabetically last.')

else:
    print('You game the same word twice.')