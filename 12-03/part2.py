from collections import Counter

# row = ['1', '0', '1', '0']
# c = Counter(row)
# most_freq = max(c.values())
# most_freq_elems = [e for e in c if c[e] == most_freq]
# return 1 if len(most_freq_elems) > 1 else most_freq
#

def most_freq(row):
    count = Counter(row)
    most_elems = [e for e in count if count[e] == max(count.values())]
    return 1 if len(most_elems) > 1 else most_elems[0]

def min_freq(row):
    count = Counter(row)
    min_elems = [e for e in count if count[e] == min(count.values())]
    return 0 if len(min_elems) > 1 else min_elems[0]

def freq(row, compare):
    count = Counter(row)
    elems = [e for e in count if count[e] == compare(count.values())]
    return compare(elems) if len(elems) > 1 else elems[0]

# EXAMPLE
# def list_sum(ls, index=0, result=0):
#     if index == len(ls):
#         return result
#     return list_sum(ls, index + 1, result + ls[index])



def oxygen_generator_rating(ls, index=0):
    if index == len(ls):
        return # SOMETHING
    # find most common bit (1 or 0)
    # if equally common, select 1
    # create list with only those where bit n is most common
    # recursion until only one list remains
    # return as int
    return oxygen_generator_rating(ls, index + 1)


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

    # todo


if __name__ == "__main__":
    main()
