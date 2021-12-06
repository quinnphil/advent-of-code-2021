import utils


def simulate_fish(fish, days):
    TIMER_RANGE = 9
    NEW_FISH_POS = 7
    school = [fish.count(f) for f in range(0, TIMER_RANGE)]
    for day in range(days):
        p0 = day % TIMER_RANGE
        school[(p0 + NEW_FISH_POS) % TIMER_RANGE] += school[p0]
    return sum(school)


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
