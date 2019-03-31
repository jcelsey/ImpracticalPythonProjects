from Chapter2 import load_dictionary


def main():
    # Load digital dictionary file as a list of words
    word_list = load_dictionary.load('../Chapter2/dictionary.txt')

    # Accept a word from a user
    user_word = input("What word would you like to find anagrams for?\n").lower()

    # Create an empty list to hold anagrams
    anagram_list = []

    # Sort the user-word
    sorted_user_word = sorted(user_word)

    # Loop through each word in the word list:
    for word in word_list:
        if len(word) != len(sorted_user_word):
            continue

        # Sort the word
        sorted_word = sorted(word.lower())

        # if word sorted is equal to user-word sorted:
        if sorted_user_word == sorted_word:
            # Append word to anagrams list
            anagram_list.append(word)

    # Print anagrams list
    if len(anagram_list) == 0:
        print("There are no anagrams for {} in the dictionary provided".format(user_word))
    else:
        print("Anagram list for {}:".format(user_word))
        print(*anagram_list, sep='\n')


if __name__ == "__main__":
    main()
