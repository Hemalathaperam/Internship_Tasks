##Q1. Find the Shortest Word in a Sentence

"""Logic: Split the sentence into words.
Assume the first word is the shortest, then compare each remaining word's length.
"""

# Observe: Input is a sentence.
# Understand: Find the word with the fewest characters.
# Break: Split the sentence and compare word lengths.
# Logic: Update the shortest word when a smaller word is found.
# Code:

sentence = "Python makes coding easy"
words = sentence.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
          shortest = word

print(shortest)
