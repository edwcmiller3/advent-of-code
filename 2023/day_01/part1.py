puzzle: list[str] = [l.strip() for l in open('input', 'r').readlines()]

def solve(puzzleInput: str) -> int:
    first_digit: str = [x for x in puzzleInput if x.isdigit()][0]
    last_digit: str = [x for x in puzzleInput if x.isdigit()][-1]
    return int(first_digit + last_digit)

print(sum([solve(line) for line in puzzle]))