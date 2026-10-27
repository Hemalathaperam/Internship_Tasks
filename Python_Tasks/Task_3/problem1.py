from solutions import q1_word_frequency

# Sample input
sample_result = q1_word_frequency("python is easy and python is powerful")
print("Sample:", sample_result)  # Expected: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

# Additional test case
extra_result = q1_word_frequency("red blue red")
print("Additional test:", extra_result)  # Expected: {'red': 2, 'blue': 1}
