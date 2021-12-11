def read_input(filename):
    with open(filename, 'r') as f:
        temp = f.read().splitlines()
        return [int(t) for t in temp if t.isnumeric()]


def count_bigger(d):
    counts = [1 for i in range(len(d) - 1) if d[i] < d[i + 1]]
    return sum(counts)


def main():
    data = read_input('input.txt')
    print(count_bigger(data))


if __name__ == "__main__":
    main()
