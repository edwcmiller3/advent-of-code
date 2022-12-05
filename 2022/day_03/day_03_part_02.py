from itertools import zip_longest
from string import ascii_letters
from typing import TextIO, Tuple


def read_file(file: TextIO) -> Tuple[str, ...]:
    """Read and clean a file returning contents as a tuple"""
    return tuple(file.read().strip().split("\n"))


def grouper(data: Tuple[str, ...], size: int) -> zip_longest:
    """Collect data into size-length chunks"""
    return zip_longest(*[iter(data)] * size)


def common_among_group(group: Tuple[str, ...]) -> str:
    """Return the string (character) common between each element of a tuple using set intersection"""
    return ''.join(set(group[0]).intersection(*group[1:]))


def priority(item: str) -> int:
    """Return index + 1 of a character in ascii_letters to determine priority of item type"""
    return ascii_letters.find(item) + 1


if __name__ == "__main__":
    total = 0
    with open("input.txt", "r") as f:
        print(
            f"Part 2: {sum((priority(common_among_group(group)) for group in grouper(read_file(f), size=3)))}")
