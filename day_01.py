import utils


def get_window(data, i, window_size):
    window = data[i: i + window_size]
    return window


def calc_increase(data, window_size):
    increased = 0
    last = 0

    for i, d in enumerate(data[:len(data) - (window_size - 1)]):
        current = sum(get_window(data, i, window_size))
        if i > 0 and current > last:
            increased += 1
        last = current

    return increased


def main():
    day = 1

    with open (f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.ints(utils.lines(fh.read()))

    print('** Test **')
    increase = calc_increase(data_test, 1)
    print(f"{increase}")
    assert(increase == 7)
    print()

    day = 1
    data = utils.ints(utils.lines(utils.read_input_file(day)))

    print('** Part 01 **')
    increase = calc_increase(data, window_size=1)
    print(f"{increase}")
    print()

    print('** Part 02 **')
    increase = calc_increase(data, window_size=3)
    print(f"{increase}")


if __name__ == "__main__":
    main()
