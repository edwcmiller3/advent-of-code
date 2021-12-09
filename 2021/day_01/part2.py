def intify_input(s):
    new_input = []
    [new_input.append(int(i)) for i in s]
    return new_input

def hof_count(window):
    def count_bigger(d):
        count = 0
        for i in range(len(d) - window):
            count += 1 if d[i] < d[i + window] else 0
        return count
    return count_bigger

def main():
    with open('input.txt', 'r') as my_file:
        data = intify_input(my_file.readlines())
    part2 = hof_count(3)
    print(part2(data))

if __name__ == "__main__":
    main()