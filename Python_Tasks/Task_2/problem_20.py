"""Q20. Find the Longest Word That Appears Only Once"""

# Observe: Input is a sentence.
# Understand: Find the longest word occurring exactly once.
# Break: Normalize case, count words, and compare lengths.
# Logic: Update only for a strictly longer qualifying word.

sentence = "Python makes coding useful Python"
words = sentence.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

longest = None

for word in words:
    if frequency[word] == 1:
        if longest is None or len(word) > len(longest):
            longest = word

if longest is not None:
    print(longest)
