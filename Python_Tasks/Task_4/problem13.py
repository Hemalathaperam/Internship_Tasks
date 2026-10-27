if __name__ == '__main__':
    n = int(input())
    set_a = set(map(int, input().split()))

    m = int(input())
    set_b = set(map(int, input().split()))

    result = sorted(set_a.symmetric_difference(set_b))
    for value in result:
        print(value)
