from typing import TextIO, Tuple
import string


def parse_input(file: TextIO) -> Tuple[str]:
    return tuple(file.read().strip().split("\n"))


def string_middle(string: str) -> int:
    return len(string) // 2


def split_rucksack(rucksack: str) -> Tuple[str, str]:
    return (rucksack[:string_middle(rucksack)], rucksack[string_middle(rucksack):])


def shared_items(rucksacks: Tuple[str, str]) -> str:
    return ''.join(set(rucksacks[0]).intersection(rucksacks[1]))


def priority(item: str) -> int:
    return string.ascii_letters.find(item) + 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(
            f"Part 1: {sum((priority(shared_items(split_rucksack(item))) for item in parse_input(f)))}")
