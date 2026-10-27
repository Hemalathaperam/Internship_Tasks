if __name__ == '__main__':
    n = int(input())
    marks = {}

    for _ in range(n):
        data = input().split()
        marks[data[0]] = list(map(float, data[1:]))

    query_name = input()
    average = sum(marks[query_name]) / len(marks[query_name])
    print(f"{average:.2f}")
