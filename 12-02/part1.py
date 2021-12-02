# def tuplify_input(f):
#     # return list(map(lambda l: tuple(l.split()), f))
#     new_list = []
#     for i in f:
#         x, y = i.split()
#         new_list.append(tuple([x, int(y)]))
#     return new_list

def tuplify(i):
    x, y = i.split()
    return tuple([x, int(y)])

def main():
    with open('input.txt', 'r') as my_file:
        # steps = tuplify_input(my_file.readlines())
        steps = map(tuplify, my_file.readlines())
    
    depth, distance = 0, 0
    for j, k in steps:
        # do something
        match j:
            case 'forward':
                distance += k
            case 'down':
                depth += k
            case 'up':
                depth -= k
    
    # output = [(x * y) for x, y in result]
    print(depth * distance)

if __name__ == "__main__":
    main()