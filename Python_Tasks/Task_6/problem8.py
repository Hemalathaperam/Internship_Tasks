# Problem: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    values = tuple(map(int, input().split()))
    print(hash(values))
