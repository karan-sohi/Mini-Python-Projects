import string

def encrypt(number, shift):
    index_list = []
    encrypted_word_list = []

    for letter in number:
        if letter != ' ':
            initial_index = ord(letter) - 97
            final_index = initial_index + shift + 97
            index_list.append(final_index)
        else:
            index_list.append(' ')
    
    for number in index_list:
        if number != ' ':
            encrypted_word_list.append(chr(number))
        else:
            encrypted_word_list.append(' ')
    
    encrypted_word = ''.join([str(item) for item in encrypted_word_list])
    return encrypted_word


def decrypt(word, shift):

    index_list = []
    decrypted_word_list = []
    
    for letter in word:
        if word != ' ':
            initial_index = ord(letter) - 97
            final_index = initial_index - shift + 97
            index_list.append(final_index)
        else:
            index_list.append(' ')

    for number in index_list:
        if number != ' ':
            decrypted_word_list.append(chr(number))
        else:
            decrypted_word_list.append(' ')
    
    decrypted_word = ''.join([str(item) for item in decrypted_word_list])
    return decrypted_word
            

def main():
    try_again = "yes"

    while try_again == "yes":
        decision = input("Type 'encode' to encrypt, type 'decode' to decrypt \n")
        if decision == 'encode':
            message = input("Type your message to encrypt \n")
            number = int(input("Type the shift number \n"))
            encrypted_word = encrypt(message, number)

            print("Here is the encoded result: ", encrypted_word)

        elif decision == 'decode':
            message = input("Type your message to decode: \n")
            number = int(input("Type the shift number \n"))
            decrypted_word = decrypt(message, number)
            print("Here is the decode result: ", decrypted_word)

        else:
            print("Wrong spelling!. \n Please try again.")

        try_again = input("Type 'yes' if you want to go again. Other type 'no'.\n")


main()


