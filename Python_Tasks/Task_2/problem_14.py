"""Q14. Dictionary of Numbers and Squares"""

# Observe: Input is a list of numbers.
# Understand: Map every number to its square.
# Break: Multiply each number by itself.
# Logic: Use a dictionary comprehension.
numbers=[1,2,3,4]
result={number:number**2 for number in numbers}
print(result)
