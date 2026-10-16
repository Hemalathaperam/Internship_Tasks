"""Q5. Find the Word with Maximum Characters"""

# Observe: Input is a sentence.
# Understand: Find the word with the maximum length.
# Break: Split into words and compare lengths.
# Logic: Keep the first word when lengths are tied.

sentence = "Data engineering requires problem solving"
words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)
