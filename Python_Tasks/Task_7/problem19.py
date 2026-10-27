"""Problem 19: Weighted Uniform Strings
HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
run = 0
for char in s:
    if char == previous:
        run += 1
    else:
        previous = char
        run = 1
    weights.add((ord(char) - ord("a") + 1) * run)

for q in queries:
    print("Yes" if q in weights else "No")
