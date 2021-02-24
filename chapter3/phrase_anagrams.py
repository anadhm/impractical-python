"""Compute phrase anagrams from a name."""
import sys
from collections import Counter
import load_dictionary
dict_file = load_dictionary.load("words.txt")
# ensure "a" and "I" (both lowercase) are included
dict_file.append("a")
dict_file.append("i")
dict_file.sort()

ini_name = input("Enter a name: ")
def find_anagrams(name, word_list):
    """Read name and dictionary file and display all anagrams in name."""
    name_letter_map = Counter(name)
    anagrams=[]
    for word in word_list:
        test=''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test+=letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Remaining letter = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams = {}".format(len(anagrams)))