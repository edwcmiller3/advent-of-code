def read_input(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in f.readlines()]


def count_bigger(d):
    counts = [1 for i in range(len(d) - 1) if d[i] < d[i + 1]]
    return sum(counts)


def main():
    data = read_input('input.txt')
    print(count_bigger(data))  # 1581


if __name__ == "__main__":
    main()
