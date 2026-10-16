"""Q16. Find the Most Frequent Word"""

# Observe: Input is a sentence.
# Understand: Find the most frequent word, ignoring case.
# Break: Convert words to lowercase and count them.
# Logic: Preserve the first word when frequencies are tied.

sentence = "Python is easy and Python is powerful"
words = sentence.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

most_frequent = words[0]

for word in words:
    if frequency[word] > frequency[most_frequent]:
        most_frequent = word

print(most_frequent)
