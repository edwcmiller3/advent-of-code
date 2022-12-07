from types import MappingProxyType
from typing import TextIO, Tuple, Dict
import typing
import re

# (move 2) (from 4) (to 6)
# repeat action - starting stack - ending stack

# import re
# re.split(r'(?<=\d)\D', 'move 2 from 4 to 6') -> ['move 2', 'from 4', 'to 6']
# 'move 2 from 4 to 6' -> ({'move': 2, 'from': 4, 'to': 6}, {...})

# find a digit where the next character is a non digit
# in 'move 2 from 4 to 6' it matches the space between '2' and 'from', and '4' and 'to'
SPLIT_RULE = r'(?<=\d)\D'


def read_file(file: TextIO) -> Tuple[str, ...]:
    """
    'move 2 from 3 to 4\n...' -> ('move 2 from 3 to 4', ...)
    """
    return tuple(file.read().strip().split('\n'))


def generate_command(commands):
    """
    ('move 2 from 3 to 4', ...) -> ({'move': 2, 'from': 3, 'to': 4}, ...)
    """
    return tuple({k: int(v) for (k, v) in zip(command.split(' ')[::2], command.split(' ')[1::2])} for command in commands)


if __name__ == "__main__":
    stacks = MappingProxyType(
        {
            # left to right = bottom to top
            1: "NBDTVGZJ",
            2: "SRMDWPF",
            3: "VCRSZ",
            4: "RTJZPHG",
            5: "TCJNDZQF",
            6: "NVPWGSFM",
            7: "GCVBPQ",
            8: "ZBPN",
            9: "WPJ"
        }
    )
