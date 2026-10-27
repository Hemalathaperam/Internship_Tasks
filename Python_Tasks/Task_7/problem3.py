"""Problem 3: Mars Exploration
HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem
"""

s = input().strip()
expected = "SOS"
changed = sum(char != expected[i % 3] for i, char in enumerate(s))
print(changed)
