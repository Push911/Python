import sys
import os


def read(argv):
    f = open(argv)
    for amount_lines, lines in enumerate(f):
        continue
    print("Amount of lines: ", amount_lines)
    print("Amount of bytes: ", os.path.getsize(argv))

    num_words = 0
    with open(argv, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    print("Number of words: ", num_words)
    print("Amount of letters in longest word: ", len(max(open(argv), key=len)))


if sys.argv[1]:
    read(sys.argv[1])
else:
    print("Please pass the paths to check as parameters to the script")



