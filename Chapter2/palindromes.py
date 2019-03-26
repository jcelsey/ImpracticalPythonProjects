"""
Load digital dictionary file as a list of words
Create an empty list to hold palindromes
Loop through each word in the word list:
    If word sliced forward is the same as word sliced backward:
        Append word to palindrome list
Print palindrome list
"""
from Chapter2 import load_dictionary


def main():
    word_list = load_dictionary.load('dictionary.txt')
    pali_list = []

    for word in word_list:
        if word[:] == word[::-1]:
            pali_list.append(word)

    print("Number of palindromes in dictionary is {}\n".format(len(pali_list)))
    print(*pali_list, sep='\n')


if __name__ == "__main__":
    main()
