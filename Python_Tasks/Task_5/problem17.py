# Problem 17: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    happy = set(map(int, input().split()))
    unhappy = set(map(int, input().split()))

    happiness = sum(1 if x in happy else -1 if x in unhappy else 0 for x in array)
    print(happiness)
