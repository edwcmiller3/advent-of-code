from collections import Counter
from operator import methodcaller


def read_file(file):
    rules_list = list(
        map(methodcaller('split', ' -> '), file.read().splitlines()))
    rules_dict = {x[0]: x[1] for x in rules_list}
    return rules_dict

# probably not correct as it returns WAY too big a polymer string
# and answer is too high
def insert_pairs(polymer, rules, times):
    if times == 0:
        return polymer
    it = [polymer[i:i+2] for i in range(0, len(polymer) - 1)]
    new_polymer = ''.join([i[0] + rules[i] + i[1]
                          for i in it if i in rules.keys()])
    return insert_pairs(new_polymer, rules, times - 1)


def result(polymer):
    count_common = Counter(polymer).most_common()
    return count_common[0][1] - count_common[-1][1]


def main():
    polymer_template = "CKKOHNSBPCPCHVNKHFFK"

    with open('input.txt', 'r') as f:
        rules = read_file(f)

    print(result(insert_pairs(polymer_template, rules, 10)))


if __name__ == "__main__":
    main()
