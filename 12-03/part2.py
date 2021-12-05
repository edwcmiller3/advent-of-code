from collections import Counter

# row = ['1', '0', '1', '0']
# c = Counter(row)
# most_freq = max(c.values())
# most_freq_elems = [e for e in c if c[e] == most_freq]
# return 1 if len(most_freq_elems) > 1 else most_freq

def oxygen_generator_rating(list, position):
    # find most common bit (1 or 0)
    # if equally common, select 1
    # create list with only those where bit n is most common
    # recursion until only one list remains
    # return as int
    return oxygen_generator_rating(list, position + 1)

def co2_scrubber_rating(list, position):
    # find least common bit (1 or 0)
    # if equally common, select 0
    # create list with only those where bit n is most common
    # recursion until only one list remains
    # return as int
    return co2_scrubber_rating(list, position + 1)

def main():
    with open('input.txt', 'r') as my_file:
        raw_diagnostic = my_file.read()

    prepared_diagnostic = [list(x) for x in raw_diagnostic.split()]
    rotated_diagnostic = [[row[i] for row in prepared_diagnostic]
                          for i in range(len(prepared_diagnostic[0]))]
    
    # todo


if __name__ == "__main__":
    main()