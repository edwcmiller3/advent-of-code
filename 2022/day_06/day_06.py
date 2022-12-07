from itertools import dropwhile
from typing import TextIO, Tuple, Generator


def read_input(file: TextIO) -> str:
    return file.read().strip()


def check_duplicates(chunk: str) -> bool:
    return True if sorted(list(chunk)) == sorted(set(chunk)) else False


def chunk_sequence(sequence: str, start: int, size: int):
    if check_duplicates(sequence[start:start + size]):
        return sequence[start:start + size]
    else:
        return chunk_sequence(sequence, start + 1, size + 1)


def find_marker(sequence: str, chunk: str) -> int:
    return sequence.rfind(chunk) + len(chunk) - 1

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        rf = read_input(f)
        c = chunk_sequence(rf, 0, 4)
        m = find_marker(rf, c)
        print(f"Marker: {m}")
# if check dupes == True return end (index of fr (+1?))
# need to pass somewhere the inpu
