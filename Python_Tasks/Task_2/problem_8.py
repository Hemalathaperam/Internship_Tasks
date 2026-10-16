"""Q8. Find the Most Frequent Character"""

# Observe: Input is a string.
# Understand: Find the most frequent character, ignoring spaces.
# Break: Count each character.
# Logic: Update the answer only when a strictly higher
# frequency is found, preserving the first character in a tie.

text = "banana"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

most_frequent = text[0]

for char in text:
    if frequency[char] > frequency[most_frequent]:
        most_frequent = char

print(most_frequent)
