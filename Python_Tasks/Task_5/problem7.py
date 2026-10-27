# Problem 7: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    m = int(input().strip())
    set_a = set(map(int, input().split()))
    n = int(input().strip())
    set_b = set(map(int, input().split()))

    result = sorted(set_a.symmetric_difference(set_b))
    for value in result:
        print(value)
