"""Q18. Find the First Word That Appears Only Once"""

# Observe: Input is a sentence.
# Understand: Find the first word occurring exactly once.
# Break: Normalize case and count each word.
# Logic: Return the first word with frequency 1.

sentence = "apple banana apple mango banana orange"
words = sentence.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word in words:
    if frequency[word] == 1:
        print(word)
        break
