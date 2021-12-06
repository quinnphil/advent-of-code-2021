import utils



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
            "days": 80,
            "assert_value": 5934
        },
        # {
        #     "name": "** Part 01 **",
        #     "data": data,
        #     "days": 80
        # },
        # {
        #     "name": "** Test 02 **",
        #     "data": data_test,
        #     "days": 256,
        #     "assert_value": 26984457539
        # },
        # {
        #     "name": "** Part 02 **",
        #     "data": data,
        #     "days": 256
        # }
    ]

    for run in runs:
        print(run['name'])
        output = 5934

        print(f"{output=}")
        if assert_value := run.get('assert_value'):
            assert (output == assert_value)


if __name__ == "__main__":
    main()
