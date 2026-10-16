"""Q9. Find the Least Frequent Character"""

# Observe: Input is a string.
# Understand: Find the least frequent character, ignoring spaces.
# Break: Count each character.
# Logic: Update the answer only when a strictly lower
# frequency is found, preserving the first character in a tie.

text = "hemalatha"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

most_frequent = text[0]

for char in text:
    if frequency[char] < frequency[most_frequent]:
        most_frequent = char

print(most_frequent)
