from random_word import RandomWords
r = RandomWords()
rnd_word = r.get_random_word().lower()
print(rnd_word)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


blank_word = ""
for element in range(0, len(rnd_word)):
    blank_word += "_"


print(logo)

rnd_word_list = list(rnd_word)
blank_word_list = list(blank_word)

stage = 6

while "_" in blank_word_list and stage > 0:

    user_input = input("Guess a letter: ")

    if user_input in rnd_word:
        indexes = [index for index, element in enumerate(rnd_word_list) if element == user_input]
        for indx in range(0, len(blank_word_list)):
            for indx1 in indexes:
                if indx == indx1:
                    blank_word_list[indx] = rnd_word[indx1]
        guessed_word = ' '.join([str(item) for item in blank_word_list])
        print(guessed_word)
    else:
        print("You guessed "+user_input+", that's not in the word. You lose a life. ")
        guessed_word = ' '.join([str(item) for item in blank_word_list])
        print(guessed_word)
        stage -= 1

    print(stages[stage])