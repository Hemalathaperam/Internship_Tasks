"""Problem 13: Sherlock and the Valid String
HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem
"""

from collections import Counter

s = input().strip()
freq_counts = Counter(Counter(s).values())

if len(freq_counts) == 1:
    print("YES")
elif len(freq_counts) == 2:
    (f1, c1), (f2, c2) = freq_counts.items()
    valid = (
        (f1 == 1 and c1 == 1) or
        (f2 == 1 and c2 == 1) or
        (abs(f1 - f2) == 1 and ((f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1)))
    )
    print("YES" if valid else "NO")
else:
    print("NO")
