"""Calculate anagrams.

Given a word (or name) from input and a dictionary file
search for and print a list of anagrams.
"""
import load_dictionary
word_list=load_dictionary.load("words.txt")
anagram_list=[]
#input a single name or word below to find its anagram
name=input("Please enter a word to search anagrams for:\n")
print("Input name = {}".format(name))
name=name.lower()
print("Using name = {}".format(name))

#sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

#print out list of anagrams
print()
if len(anagram_list)==0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =",*anagram_list,sep='\n')