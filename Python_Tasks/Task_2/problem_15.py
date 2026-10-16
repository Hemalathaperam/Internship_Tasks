"""Q15. Dictionary of Numbers and Even/Odd Status"""

# Observe: Input is a list of integers.
# Understand: Identify each number as Even or Odd.
# Break: Check the remainder after division by 2.
# Logic: Remainder 0 means Even; otherwise Odd.
numbers = [1, 2, 3, 4, 5]

result = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print(result)
