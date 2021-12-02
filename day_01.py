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

    print('** Test **')  # 1451
    test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print(calc_increase(test_data, 1))
    print()

    day = 1
    data = utils.ints(utils.lines(utils.read_input_file(day)))

    print('** Part 01 **')  # 1451
    print(calc_increase(data, window_size=1))
    print()

    print('** Part 02 **')  # 1379
    print(calc_increase(data, window_size=3))
    print()


if __name__ == "__main__":
    main()
