"""Q19. Count Words Longer Than Four Characters"""

# Observe: Input is a sentence.
# Understand: Count words with more than four characters.
# Break: Split the sentence and check each word's length.
# Logic: Increase the count when len(word) > 4.

sentence = "Python makes problem solving interesting"
words = sentence.split()
count = 0

for word in words:
    if len(word) > 4:
        count += 1

print(count)
