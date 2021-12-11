def read_input(filename):
    with open(filename, 'r') as f:
        temp = f.read().splitlines()
        return [int(t) for t in temp if t.isnumeric()]


def hof_count(window):
    def count_bigger(d):
        count = [1 for i in range(len(d) - window) if d[i] < d[i + window]]
        return sum(count)
    return count_bigger


def main():
    data = read_input('input.txt')
    part2 = hof_count(3)
    print(part2(data))


if __name__ == "__main__":
    main()
