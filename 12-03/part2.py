from collections import Counter

# def most_freq(row):
#     count = Counter(row)
#     most_elems = [e for e in count if count[e] == max(count.values())]
#     return 1 if len(most_elems) > 1 else most_elems[0]

# def min_freq(row):
#     count = Counter(row)
#     min_elems = [e for e in count if count[e] == min(count.values())]
#     return 0 if len(min_elems) > 1 else min_elems[0]

# def freq(row, compare):
#     count = Counter(row)
#     elems = [e for e in count if count[e] == compare(count.values())]
#     return compare(elems) if len(elems) > 1 else elems[0]


def hof_freq(compare):
    def freq(row):
        count = Counter(row)
        elems = [e for e in count if count[e] == compare(count.values())]
        return compare(elems) if len(elems) > 1 else elems[0]
    return freq

# EXAMPLE
# def list_sum(ls, index=0, result=0):
#     if index == len(ls):
#         return result
#     return list_sum(ls, index + 1, result + ls[index])


def oxygen_generator_rating(ls, index=0):
    # find most common bit (1 or 0)
    # if equally common, select 1
    # create list with only those where bit n is most common
    # recursion until only one list remains
    # return as int
    # From https://github.com/Vasile-Hij/AOC-2021/blob/main/scripts/3.py
    new_ls = [l for l in ls if l[index] == f]
    return new_ls[0] if len(new_ls) == 1 else oxygen_generator_rating(ls, index + 1)


def co2_scrubber_rating(ls, index=0):
    # find least common bit (1 or 0)
    # if equally common, select 0
    # create list with only those where bit n is most common
    # recursion until only one list remains
    # return as int
    return co2_scrubber_rating(ls, index + 1)


def main():
    with open('input.txt', 'r') as my_file:
        raw_diagnostic = my_file.read()

    prepared_diagnostic = [list(x) for x in raw_diagnostic.split()]
    rotated_diagnostic = [[row[i] for row in prepared_diagnostic]
                          for i in range(len(prepared_diagnostic[0]))]

    max_freq = hof_freq(max)
    min_freq = hof_freq(min)

    # oxy = int(''.join([max_freq(r) for r in rotated_diagnostic]), 2)
    # co2 = int(''.join([min_freq(s) for s in rotated_diagnostic]), 2)



if __name__ == "__main__":
    main()