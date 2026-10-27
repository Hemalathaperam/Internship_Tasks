"""Problem 17: Separate the Numbers
HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem
"""

def separate_numbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        built = ""
        while len(built) < len(s):
            built += str(current)
            current += 1
        if built == s:
            print(f"YES {first}")
            return
    print("NO")

for _ in range(int(input())):
    separate_numbers(input().strip())
