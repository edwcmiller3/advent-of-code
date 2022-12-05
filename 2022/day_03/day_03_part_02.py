from itertools import islice, zip_longest
from string import ascii_letters
from typing import TextIO, Tuple


def read_file(file: TextIO) -> Tuple[str, ...]:
    return tuple(file.read().strip().split("\n"))

def grouper(data: Tuple[str, ...], size: int) -> zip_longest:
    """Collect data into size-length chunks"""
    return zip_longest(*[iter(data)] * size)


def common_among_group(group: Tuple[str, ...]) -> str:
    """Return the string (character) common between each element of a tuple using set intersection"""
    return ''.join(set(group[0]).intersection(*group[1:]))


def priority(item: str) -> int:
    """Return index + 1 of a character in ascii_letters"""
    return ascii_letters.find(item) + 1


if __name__ == "__main__":
    # with open("input.txt", "r") as f:
    #     print(
    #         f"Part 1: {sum((priority(common_among_group(make_groups(item, 3))) for item in parse_input(f)))}")
    with open("input.txt", "r") as f:
        [print(x) for x in common_among_group(y) for y in grouper(read_file(f), size=3))]
        # process next_n_lines

# open file
# read first N lines (tuple)
# create new tuple with trimmed lines
# find common
# determine priority from common
# next N lines