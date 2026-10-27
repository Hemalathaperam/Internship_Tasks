# Problem: Check Subset
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = set(input().split())
        m = int(input())
        b = set(input().split())
        print(a.issubset(b))
