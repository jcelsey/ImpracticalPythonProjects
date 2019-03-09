def main():
    print('Welcome to pig latin!\n')
    print('This program will turn any word you type into pig latin.\n')

    vowels = ('a', 'e', 'i', 'o', 'u', 'y')  # vowels tuple to compare against the first letter of the word

    while True:
        word = input('Enter a word to convert to pig latin:\n')

        latin_word = ''

        if vowels.__contains__(word[0]):
            latin_word = word + 'way'
        else:
            latin_word = word[1:] + word[0] + 'ay'

        print('"{}" in pig latin is "{}"\n'.format(word, latin_word))

        try_again = input('Try again? (Press Enter else n to quit)\n ')
        if try_again.lower() == 'n':
            break

    input("Press any key to exit")


if __name__ == '__main__':
    main()
