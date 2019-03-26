"""Load a text file as a list.

Arguments:
    -text file name (and directory path, if needed)

Exceptions:
    -IOError if filename not found

Returns:
    -A list of all words in a text files in lower case
"""

import sys


def load(file):
    """Open a text file & return a list of lowercase string."""

    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}".format(e, file))
        sys.exit(1)
