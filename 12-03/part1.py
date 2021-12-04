from collections import Counter


def freq(flag):
    def count_freq(l):
        # a = Counter('010111')
        # a.most_common(1)[0][1] // 4
        match flag:
            case 'max':
                return Counter(l).most_common()[0][0]
            case 'min':
                return Counter(l).most_common()[-1][0]
            case _:
                raise ValueError
    return count_freq


def main():
    with open('input.txt', 'r') as my_file:
        raw_diagnostic = my_file.read()

    prepared_diagnostic = [list(x) for x in raw_diagnostic.split()]
    rotated_diagnostic = [[row[i] for row in prepared_diagnostic]
                          for i in range(len(prepared_diagnostic[0]))]

    gamma, epsilon = [], []
    max_freq = freq('max')
    min_freq = freq('min')

    [gamma.append(max_freq(r)) for r in rotated_diagnostic]
    [epsilon.append(min_freq(r)) for r in rotated_diagnostic]

    print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))


if __name__ == "__main__":
    main()
