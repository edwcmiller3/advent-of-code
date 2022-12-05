from typing import TextIO, Tuple

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

def section_ranges(sections: str) -> Tuple[int, ...]:
    """Takes a sections ('9-61') and creates a tuple of ranges"""
    return (1,2,3)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        #tuple(print(i.split(',')) for i in read_file(f))
        #print(f.read()[0])
        print(read_file(f))