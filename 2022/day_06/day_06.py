from typing import TextIO




def read_input(file: TextIO) -> str:
    return file.read().strip()


# def check_duplicates(chunk: str, size: int) -> bool:
#     return True if len(set(chunk)) == size else False

def unique_chunk_length(chunk: str) -> int:
    return len(set(chunk))



def parse_sequence(sequence: str, size: int) -> int:
    yield next [i + size for i in range(len(sequence)) if unique_chunk_length(sequence[i:i + size]) == size]
    #return i + size if (unique_chunk_length(sequence[i:i + size]) == size) for i in range(len(sequence)) else False

# from https://stackoverflow.com/a/73094705
# def sliding_window(iterable, n):
#     # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
#     it = iter(iterable)
#     window = collections.deque(islice(it, n), maxlen=n)
#     if len(window) == n:
#         yield tuple(window)
#     for x in it:
#         window.append(x)
#         yield tuple(window)


# leaving for posterity since it was a nice idea
# def chunk_sequence(sequence: str, start: int, size: int):
#     if check_duplicates(sequence[start:start + size]):
#         return sequence[start:start + size]
#     else:
#         return chunk_sequence(sequence, start + 1, size + 1)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(f"Part 1: {parse_sequence(read_input(f), 4)}")
# if check dupes == True return end (index of fr (+1?))
# need to pass somewhere the inpu
