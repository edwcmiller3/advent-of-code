def tuplify(i):
    x, y = i.split()
    return tuple([x, int(y)])

def main():
    with open('input.txt', 'r') as my_file:
        steps = map(tuplify, my_file.readlines())
    
    depth, distance, aim = 0, 0, 0
    for j, k in steps:
        match j:
            case 'forward':
                distance += k
                depth += aim * k
            case 'down':
                aim += k
            case 'up':
                aim -= k
    
    # output = [(x * y) for x, y in result]
    print(depth * distance)

if __name__ == "__main__":
    main()