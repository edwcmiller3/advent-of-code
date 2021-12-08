from math import ceil
from statistics import median


def calc_least_cost_pos(ls):
    return ceil(median(ls))


def calc_fuel(c, pos):
    return abs(c - pos)


def main():
    with open('input.txt', 'r') as crab_file:
        crabs = list(map(int, crab_file.readline().split(',')))

    least_cost_pos = calc_least_cost_pos(crabs)

    fuel_costs = sum([calc_fuel(crab, least_cost_pos) for crab in crabs])

    print(fuel_costs)


if __name__ == "__main__":
    main()
