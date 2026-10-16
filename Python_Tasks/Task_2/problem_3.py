"""Q3. Find the Smallest Number Without min()

Logic: Start with the first number and update the smallest value whenever a smaller number is found.
"""

# Observe: Input is a list of numbers.
# Understand: Find the smallest number without min().
# Break: Compare each number with the current smallest.
# Logic: Replace the smallest when a smaller number is found.

numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)
