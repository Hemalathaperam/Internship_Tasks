"""Problem 11: Two Strings
HackerRank: https://www.hackerrank.com/challenges/two-strings/problem
"""

for _ in range(int(input())):
    s1 = set(input().strip())
    s2 = set(input().strip())
    print("YES" if s1 & s2 else "NO")
