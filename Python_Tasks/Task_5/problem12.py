# Problem 12: Capitalize!
# HackerRank: https://www.hackerrank.com/challenges/capitalize/problem

import os

def solve(s):
    return ' '.join(word[:1].upper() + word[1:] for word in s.split(' '))

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
