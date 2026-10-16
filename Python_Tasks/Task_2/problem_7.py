"""Q7. Count Consonants"""

# Observe: Input can contain letters, digits, and symbols.
# Understand: Count consonants only.
# Break: Check alphabetic characters and exclude vowels.
# Logic: Use isalpha() and a vowel membership check.

text = "Python 123!"
count = 0

for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        count += 1

print(count)
