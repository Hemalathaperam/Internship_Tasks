"""Q6. Count Vowels in a String"""

# Observe: Input is a string.
# Understand: Count uppercase and lowercase vowels.
# Break: Check every character.
# Logic: Count characters present in "aeiou".

text = "innomatics"
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)
