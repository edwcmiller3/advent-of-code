from typing import TextIO, Tuple


def parse_input(file: TextIO) -> Tuple[Tuple[str]]:
    return tuple(tuple(groups.split("\n")) for groups in file.read().strip().split("\n\n"))


def tuple_str_to_int(tupstr: Tuple[Tuple[str]]) -> Tuple[Tuple[int]]:
    # return tuple(int(item) for item in tupstr)
    return tuple(tuple(map(int, x)) for x in tupstr)


def solve_part1(input: Tuple[Tuple[int]]) -> int:
    return tuple(sorted(sum(t) for t in input))[-1]


def solve_part2(input: Tuple[Tuple[int]]) -> int:
    return sum(tuple(sorted(sum(t) for t in input))[-3:])


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        print(f"Part 1: {solve_part1(tuple_str_to_int(parse_input(f)))}")

    with open("input.txt", "r") as f:
        print(f"Part 2: {solve_part2(tuple_str_to_int(parse_input(f)))}")
