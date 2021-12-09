from statistics import mean


def calc_least_cost_pos(ls):
    return int(mean(ls))


def calc_fuel(c, pos):
    # Triangle numbers maths
    # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/runsums/triNbProof.html
    fuels = (abs(c - pos) * (abs(c - pos) + 1)) // 2
    return fuels


def main():
    with open('input.txt', 'r') as crab_file:
        crabs = list(map(int, crab_file.readline().split(',')))

    least_cost_pos = calc_least_cost_pos(crabs)

    fuel_costs = sum([calc_fuel(crab, least_cost_pos) for crab in crabs])

    print(fuel_costs)


if __name__ == "__main__":
    main()
