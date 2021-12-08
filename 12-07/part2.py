# for each starting point
# calc distance to lowest cost point
# create a list of the range
# e.g. [i for i in range(distance + 1)]
# sum the range to calculate total fuel cost for that point
# next starting point

# from statistics import mean
# or sum([calc_fuel(crab, least_cost_pos) for crab in crabs]) / len(crabs)
# probably slap ceil() around that as well

from math import ceil
from statistics import mean


def calc_least_cost_pos(ls):
    return ceil(mean(ls))


def calc_fuel(c, pos):
    fuels = [i for i in range(1, ceil(abs(c - pos) + 1))]
    return sum(fuels)


def main():
    with open('input.txt', 'r') as crab_file:
        crabs = list(map(int, crab_file.readline().split(',')))

    least_cost_pos = calc_least_cost_pos(crabs)

    fuel_costs = sum([calc_fuel(crab, least_cost_pos) for crab in crabs])

    print(fuel_costs)


if __name__ == "__main__":
    main()
