from collections import Counter


def ratings(ls, fn, index=0):
    # Big thanks to https://github.com/Vasile-Hij/AOC-2021/blob/main/scripts/3.py
    count = fn(Counter([l[index] for l in ls]).most_common(), key=lambda x: (x[1], x[0]))[0]
    new_ls = [l for l in ls if l[index] == count]
    return new_ls[0] if len(new_ls) == 1 else ratings(new_ls, fn, index + 1)


def main():
    with open('input.txt', 'r') as my_file:
        diagnostic = [line.strip() for line in my_file.readlines()]
    
    oxygen_generator_rating = int(ratings(diagnostic, max), 2)
    co2_scrubber_rating = int(ratings(diagnostic, min), 2)
    
    print(oxygen_generator_rating * co2_scrubber_rating)


if __name__ == "__main__":
    main()
