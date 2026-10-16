"""Q17. Find All Repeated Words"""

# Observe: Input is a sentence.
# Understand: Find repeated words without duplicates.
# Break: Normalize case and count each word.
# Logic: Collect repeated words in first-appearance order.

sentence = "data science uses data and science tools"
words = sentence.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

repeated = []

for word in words:
    if frequency[word] > 1 and word not in repeated:
        repeated.append(word)

print(repeated)
