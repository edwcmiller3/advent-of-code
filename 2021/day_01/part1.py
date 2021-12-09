def intify_input(s):
    new_input = []
    [new_input.append(int(i)) for i in s]
    return new_input

def count_bigger(d):
    count = 0
    for i in range(len(d) - 1):
        count += 1 if d[i] < d[i + 1] else 0
    return count

def main():
    with open('input.txt', 'r') as my_file:
        data = intify_input(my_file.readlines())
    print(count_bigger(data))

if __name__ == "__main__":
    main()