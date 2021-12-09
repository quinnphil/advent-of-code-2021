import utils


def get_best_alignment(crab_positions, with_increment=False):
    crabs = dict()
    alignments = dict()

    for i in crab_positions:
        crabs[i] = crabs.get(i, 0) + 1

    for destination in range(0, max(crabs.keys()) + 1):
        fuel_total = 0

        for source in crabs:
            distance = abs(source - destination)
            if not with_increment:
                # Move cost is 1
                fuel_cost = distance * crabs[source]
            else:
                fuel_cost = int(distance * (1 + distance) / 2) * crabs[source]
            fuel_total += fuel_cost
        alignments[destination] = fuel_total

    min_crab, min_fuel = (min(alignments, key=alignments.get), min(alignments.values()))

    return min_crab, min_fuel


def main():
    day = 7

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 37,
            "increment": False
        },
        {
            "name": "** Part 01 **",
            "data": data,
            "days": 80,
            "increment": False
        },
        {
            "name": "** Test 02 **",
            "data": data_test,
            "assert_value": 168,
            "increment": True
        },
        {
            "name": "** Part 02 **",
            "data": data,
            "increment": True
        },
    ]

    for run in runs:
        print(run['name'])
        (position, fuel) = get_best_alignment(run['data'], with_increment=run['increment'])
        print(f"{position=}")
        print(f"{fuel=}")
        if assert_value := run.get('assert_value'):
            assert (fuel == assert_value)


if __name__ == "__main__":
    main()
