"""Q11. Dictionary of Words and First Characters"""

# Observe: Input is a sentence.
# Understand: Map each word to its first character.
# Break: Split the sentence and access index 0.
# Logic: Use a dictionary comprehension.

sentence = "Python Data Engineering"
words = sentence.split()

result = {word: word[0] for word in words}

print(result)
