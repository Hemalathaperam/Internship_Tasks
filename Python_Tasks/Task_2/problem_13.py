"""Q13. Dictionary of Words and Uppercase Versions"""

# Observe: Input is a sentence.
# Understand: Map every word to its uppercase version.
# Break: Split into words and apply upper().
# Logic: Use each original word as the key.
sentence = "Python Data Engineering"
words = sentence.split()

result = {word: word.upper() for word in words}

print(result)
