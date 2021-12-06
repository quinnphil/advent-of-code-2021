import utils


def simulate_fish(fish_initial, days):
    school = [0] * 9

    for f in fish_initial:
        school[f] += 1

    p0 = 0  # Zero position
    for day in range(days):
        # Add pos_0 fish to pos_7
        school[(p0 + 7) % 9] += school[p0]
        # Update p0
        p0 = (p0 + 1) % 9

    fish_count = (sum(school))

    return fish_count


def main():
    day = 6

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "days": 80,
            "assert_value": 5934
        },
        {
            "name": "** Part 01 **",
            "data": data,
            "days": 80
        },
        {
            "name": "** Test 02 **",
            "data": data_test,
            "days": 256,
            "assert_value": 26984457539
        },
        {
            "name": "** Part 02 **",
            "data": data,
            "days": 256
        }
    ]

    for run in runs:
        print(run['name'])
        fish_count = simulate_fish(run['data'], run['days'])

        print(f"{fish_count=}")
        if assert_value := run.get('assert_value'):
            assert (fish_count == assert_value)


if __name__ == "__main__":
    main()
