"""Q4. Find the First Longest Word

Logic: Update the longest word only when a strictly longer word appears. This preserves the first word when lengths are tied.
"""

# Observe: Input is a sentence.
# Understand: Find the longest word, preferring the first in a tie.
# Break: Split the sentence and compare lengths.
# Logic: Update only when len(word) > len(longest).

sentence = "Python makes coding useful"
words = sentence.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)
