# Problem 18: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    length = len(string)

    for i, char in enumerate(string):
        if char in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)
