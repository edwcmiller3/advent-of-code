from typing import TextIO, Tuple, Set


def read_file(file: TextIO) -> Tuple[Tuple[str, ...]]:
    """Read and clean a file returning contents as a tuple of tuples"""
    return tuple(tuple(ag.split(',')) for ag in file.read().strip().split("\n"))


def parse_range(section_range: str, splitter: str) -> Tuple[str, str]:
    """Takes a section_range like '10-15' and a spliiter like '-' then
    returns a tuple with each part of the split section_range"""
    return tuple(section_range.split(splitter))


def generate_range_set(parsed_range: Tuple[str, str]) -> Set[int]:
    """Takes a parsed_range like ('9', '61') and returns a set of a 
    range from parsed_range[0] through parsed_range[1] inclusive"""
    return set(range(int(parsed_range[0]), int(parsed_range[1]) + 1))


def find_subsets(range_set_A: Set[int], range_set_B: Set[int]) -> int:
    """Compare 2 sets and return 1 if either is a subset of the other 
    otherwise return 0"""
    return 1 if (range_set_A.issubset(range_set_B) or range_set_B.issubset(range_set_A)) else 0


def find_overlap(range_set_A: Set[int], range_set_B: Set[int]) -> int:
    """Compare 2 sets and return 1 if either set share a member
    otherwise return 0"""
    return 0 if range_set_A.isdisjoint(range_set_B) else 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(f"Part 1: {sum((find_subsets(generate_range_set(parse_range(range_A, '-')), generate_range_set(parse_range(range_B, '-'))) for (range_A, range_B) in read_file(f)))}")

    with open("input.txt", "r") as f:
        print(f"Part 2: {sum((find_overlap(generate_range_set(parse_range(range_A, '-')), generate_range_set(parse_range(range_B, '-'))) for (range_A, range_B) in read_file(f)))}")
