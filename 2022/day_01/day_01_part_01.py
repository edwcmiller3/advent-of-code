from typing import TextIO, Tuple


def parse_input(file: TextIO) -> Tuple[Tuple[str]]:
    return tuple(tuple(groups.split("\n")) for groups in file.read().strip().split("\n\n"))


def tuple_str_to_int(tupstr: Tuple[Tuple[str]]) -> Tuple[Tuple[int]]:
    # return tuple(int(item) for item in tupstr)
    return tuple(tuple(map(int, x)) for x in tupstr)


def solve(input: Tuple[Tuple[int]]) -> int:
    return tuple(sorted(sum(t) for t in input))[-1]


with open("input.txt", 'r') as f:
    print(solve(tuple_str_to_int(parse_input(f))))
