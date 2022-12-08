from collections import deque
from itertools import islice
from typing import TextIO, Tuple


def read_input(file: TextIO) -> str:
    return file.read().strip()


def unique_chunk_length(chunk: str) -> int:
    return len(set(chunk))


def find_signal(sequence: str, size: int):
    for n in range(size, len(sequence)):
        if unique_chunk_length(sequence[n - size:n]) == size:
            return n


# leaving for posterity since it was a nice idea
# def chunk_sequence(sequence: str, start: int, size: int):
#     if check_duplicates(sequence[start:start + size]):
#         return sequence[start:start + size]
#     else:
#         return chunk_sequence(sequence, start + 1, size + 1)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(f"Part 1: {find_signal(read_input(f), 4)}")
    
    with open("input.txt", "r") as f:
        print(f"Part 2: {find_signal(read_input(f), 14)}")