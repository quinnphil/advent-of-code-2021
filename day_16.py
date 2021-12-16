import re


def main():
    day = 16

    # with open(f'input/day_{day:02d}_test.txt') as fh:
    #     data_test = [[int(x) for x in line] for line in fh.read().splitlines()]
    #
    # with open(f'input/day_{day:02d}.txt') as fh:
    #     data = [[int(x) for x in line] for line in fh.read().splitlines()]
    #


    runs = [
        {
            "name": "** Test 01 **",
            # "data": data_test,
            "assert_value": 10

        },
        # {
        #     "name": "** Part 01 **",
        #     "data": data,
        #
        # },


    ]



    for run in runs:

        print(run['name'])




if __name__ == "__main__":
    main()







