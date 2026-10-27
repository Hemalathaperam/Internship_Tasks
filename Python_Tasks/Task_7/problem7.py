"""Problem 7: Alphabet Rangoli
HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []
    for i in range(size):
        row = "-".join(alphabet[size - 1:size - i - 1:-1] + alphabet[size - i - 1:size])
        lines.append(row.center(width, "-"))
    print("\n".join(lines + lines[-2::-1]))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
