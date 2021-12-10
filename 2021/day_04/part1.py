# Part 1 Rules
# Winning board = 1+ complete row / column of marked numbers
# Score = sum(winning board unmarked numbers)
# Choose first winning board and determine score for that board
import pprint

def main():
    with open('numbers.txt', 'r') as numbers:
        draw = numbers.readline()
    
    # with open('boards.txt', 'r') as board_set:
    #     boards = board_set.read().split('\n\n')

    with open('boards.txt', 'r') as board_set:
        #boards = [[c for c in l.split() if c != '\n\n'] for l in board_set.readlines()]
        boards = board_set.read().split('\n\n')

    formatted_board = [[line.split() for line in board.split('\n')] for board in boards]
    final_board = [[[int(elt) for elt in line] for line in board] for board in formatted_board]

    #print(draw)
    #print(boards)
    pprint.pprint(final_board)


if __name__ == "__main__":
    main()