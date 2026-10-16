"""Q10. Find All Repeated Characters"""

# Observe: Input is a string.
# Understand: Find repeated characters without duplicates.
# Break: Count characters and preserve their first appearance.
# Logic: Add characters whose frequency is greater than one.

text = "programming".replace(" ", "")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

repeated = []

for char in text:
    if frequency[char] > 1 and char not in repeated:
        repeated.append(char)

print(repeated)
