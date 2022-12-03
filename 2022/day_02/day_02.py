from typing import TextIO, Tuple

# OPPONENT
# A: Rock
# B: Paper
# C: Scissor
#
# YOU
# X: Rock
# Y: Paper
# Z: Scissor
# 
# SCORING
# Rock = 1
# Paper = 2
# Scissor = 3
# Loss = 0
# Tie = 3
# Win = 6

def parse_input(file: TextIO) -> Tuple[Tuple[str]]:
    return tuple(tuple(rounds.split(' ')) for rounds in file.read().strip().split("\n"))

# def score

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        parse_input(f)