# read each line of input (tuple of strings?)
# split each line into 2 strings (part_a = line[int(midpoint):])
# use counter? to count occurences? - see 2021 similar puzzle (Counter().most_common())
# easier - use list comprehension
# more fun - try set intersection
#
# string1 = 'abcd'
# string2 = 'abzx'
# common_characters = ''.join(
#     set(string1).intersection(string2)
# )
# print(common_characters)  



from typing import TextIO, Tuple

def parse_input(file: TextIO) -> Tuple[str]:
    return tuple(file.read().strip().split("\n"))

def split_rucksack(rucksack: Tuple[str]) -> Tuple[Tuple[str]]:
    return True


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(True)