#!/usr/local/bin/python3

test_raw = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

test = list(test_raw.split("\n\n"))
real = list(open("4.txt").read().split("\n\n"))

def score_bingo(sections, last_to_win = False):
    numbers = [int(num) for num in sections[0].split(",")]
    boards = [[list(map(int, row.split())) for row in board.split("\n")] for board in sections[1:]]
    marksets = [[[0] * 5 for j in range(5)] for k in range(len(boards))]

    last_bingo_score = 0
    bingo_indices = set()

    for number in numbers:
        for i, board in enumerate(boards):
            if i in bingo_indices:
                continue

            marksets[i] = mark_board(board, number, marksets[i])

            if check_for_bingo(marksets[i]):
                if last_to_win:
                    bingo_indices.add(i)
                    last_bingo_score = number * sum_of_unmarked(boards[i], marksets[i])
                else:
                    return number * sum_of_unmarked(boards[i], marksets[i])

    return last_bingo_score


def mark_board(board, number, markset):
    for i in range(5):
        for j in range(5):
            if number == board[i][j]:
                markset[i][j] = 1
                return markset

    return markset


def check_for_bingo(markset):

    #check for row bingos
    for i in range(5):
        if sum(markset[i]) == 5:
            return True

    #check for column bingos
    for j in range(5):
        if sum([markset[k][j] for k in range(5)]) == 5:
            return True

    return False


def sum_of_unmarked(board, markset):
    total = 0
    for i in range(5):
        for j in range(5):
            if markset[i][j] == 0:
                total += board[i][j]

    return total

# 1
print(score_bingo(test))
print(score_bingo(real))

# 2
print(score_bingo(test, True))
print(score_bingo(real, True))
