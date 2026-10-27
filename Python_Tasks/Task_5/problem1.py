if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))
    scores = sorted(set(arr))
    print(scores[-2])
