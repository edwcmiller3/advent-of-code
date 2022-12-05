from typing import TextIO, Tuple, Set

# In how many assignment pairs does one range fully contain the other?
# use one of these:
#
# isdisjoint(other)
#     Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

# issubset(other)
# set <= other
#     Test whether every element in the set is in other.

# set < other
#     Test whether the set is a proper subset of other, that is, set <= other and set != other.

# issuperset(other)
# set >= other
#     Test whether every element in other is in the set.


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


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        read = read_file(f)
        total = 0
        for i, j in read:
            # i is range A, j is range B
            total += find_subsets(generate_range_set(parse_range(i, '-')),
                                  generate_range_set(parse_range(j, '-')))
        print(f"Total: {total}")
