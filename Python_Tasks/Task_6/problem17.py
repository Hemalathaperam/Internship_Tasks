# Problem: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    a = set(input().split())
    result = True
    for _ in range(int(input())):
        other = set(input().split())
        if not (a > other):
            result = False
            break
    print(result)
