import pprint
from collections import defaultdict


def main():
    print('This program will print the number of times a character occurs in the form of a bar chart')

    phrase = input('Enter a phrase to see how many of each letter is in the phrase:\n')

    split_phrase = list(''.join(phrase.lower().split()))

    d = defaultdict(list)

    for x in split_phrase:
        d[x].append(x)

    pprint.pprint(d)


if __name__ == '__main__':
    main()
