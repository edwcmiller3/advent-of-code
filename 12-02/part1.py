# output = [(x * y) for x, y in result]

# var horizontal, vertical
# forward operation = add
# down operation = add
# up operation = subtract

# ylist = [tuple(map(float, i.split(','))) for i in f]
# new_input = []
#     [new_input.append(int(i)) for i in s]
#     return new_input
import operator

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

def traverse(op):
    pass

def main():
    with open('input.txt', 'r') as my_file:
        #steps = tuplify_input(my_file.readlines())
        steps = map(tuplify, my_file.readlines())
    depth, distance = 0, 0
    ops = {
        'forward': operator.add,
        'down': operator.add,
        'up': operator.sub
    }
    [print(step) for step in steps]
    print(steps)

if __name__ == "__main__":
    main()