"""Q2. Find the Largest Number Without max()

Logic: Start with the first number and update the largest value whenever a bigger number is found.
"""

# Observe: Input is a list of numbers.
# Understand: Find the largest number without max().
# Break: Compare each number with the current largest.
# Logic: Replace the largest when a bigger number is found.

numbers = [12, 45, 7, 89, 23]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
