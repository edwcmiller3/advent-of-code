from operator import methodcaller


def read_file(file):
    rules_list = list(
        map(methodcaller('split', ' -> '), file.read().splitlines()))
    rules_dict = {x[0]: x[1] for x in rules_list}
    # return rules_dict
    print(rules_dict)


def main():
    polymer_template = "CKKOHNSBPCPCHVNKHFFK"

    with open('input.txt', 'r') as f:
        read_file(f)


if __name__ == "__main__":
    main()
