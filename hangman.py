from random_word import RandomWords
r = RandomWords()
rnd_word = r.get_random_word().lower()
print(rnd_word)

blank_word = ""
for element in range(0, len(rnd_word)):
    blank_word += "_"

rnd_word_list = list(rnd_word)
blank_word_list = list(blank_word)
print(rnd_word_list)
print(blank_word_list)

while "_" in blank_word_list:
    user_input = input("Guess any letter from the word: ")

    if user_input in rnd_word:
        indexes = [index for index, element in enumerate(rnd_word_list) if element == user_input]
        print(indexes)
        for indx in range(0, len(blank_word_list)):
            for indx1 in indexes:
                if indx == indx1:
                    blank_word_list[indx] = rnd_word[indx1]
                    print("yes")
        print(blank_word_list)

    else:
        print("Nothing, Try again!")