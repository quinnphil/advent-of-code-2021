import utils

def get_best_alignment(crabs, increment=0):
    print(crabs)
    all = {}
    min_fuel = -1
    min_crab = 0

    cache = {}

    for crab in crabs:
        if not all.get(crab):
            all[crab] = 1
        else:
            all[crab] += 1
    print(all)
    for align_on in range(0, max(all.keys())):
        fuel_total = 0
        cost_paths = {}
        for c_from in all:
            fuel_cost = 0
            if c_from == align_on:
                continue
            else:
                distance = abs(c_from - align_on)
                if increment == 0:
                    fuel_cost = distance * all[c_from]
                else:
                    if not cache.get((all[c_from], distance)):
                        for i in range(1, distance + 1):
                            move_cost = (i) * all[c_from]
                            fuel_cost += move_cost
                        cache[(all[c_from], distance)] = fuel_cost
                    fuel_cost = cache[(all[c_from], distance)]
            fuel_total += fuel_cost


        if min_fuel == -1:
            min_fuel = fuel_total
            min_crab = align_on
        elif fuel_total < min_fuel:
            min_fuel = fuel_total
            min_crab = align_on
    return (min_crab, min_fuel)






def main():
    day = 7

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [int(f) for f in utils.lines(fh.read())[0].split(',')]
    print(data)

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 37,
            "increment": 0
        },
        {
            "name": "** Part 01 **",
            "data": data,
            "days": 80,
            "increment": 0
        },
        {
            "name": "** Test 02 **",
            "data": data_test,
            "assert_value": 168,
            "increment": 1
        },
        {
            "name": "** Part 02 **",
            "data": data,
            "increment": 1
        },
    ]

    for run in runs:
        print(run['name'])
        (min_crab, min_fuel) = get_best_alignment(run['data'], increment=run['increment'])
        print(f"{min_crab=}")
        print(f"{min_fuel=}")
        if assert_value := run.get('assert_value'):
            assert (min_fuel == assert_value)


if __name__ == "__main__":
    main()
