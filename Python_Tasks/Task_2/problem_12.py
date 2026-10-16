"""Q12. Dictionary of Words and Last Characters"""

# Observe: Input is a sentence.
# Understand: Map each word to its last character.
# Break: Split the sentence and access index -1.
# Logic: Use word[-1] as the dictionary value.

sentence = "Python Data Engineering"
words = sentence.split()

result = {word: word[-1] for word in words}

print(result)
