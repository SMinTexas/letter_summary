# Write a script that takes a word as its input, and returns a dictionary
# containing the tally of how many times each letter in the alphabet was
# used in the word.
#
# For example:
# {'a': 3, 'b': 1, 'n': 2} # ex: banana

input_word = input("Enter a word ")

def letter_count(str):
    counts = dict((letter,str.count(letter)) for letter in set(str))
    return counts

count_of_letters = letter_count(input_word)
print(count_of_letters)
