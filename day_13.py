import utils


def parse_data(data):
    print(f'{data=}')
    dots = {}
    folds = []

    for line in data:
        if "fold along" in line:
            line = line.replace('fold along ', '')
            orientation, l = line.strip().split('=')
            l = int(l)
            folds.append((orientation, l))
        elif len(line) > 3:

            x, y = line.strip().split(',')

            dots[(int(x), int(y))] = 1

    return dots, folds


def do_fold(dots, fold):

    new_dots = {}

    direction = fold[0]
    line_position = fold[1]

    if direction == 'y':
        for dot in dots:
            dot_x = dot[0]
            dot_y = dot[1]
            if dot_y > line_position:
                # Move the dot up
                new_x = dot_x
                dif_y = dot_y - line_position
                new_y = line_position - dif_y
                if not new_dots.get((new_x, new_y)):
                    new_dots[(new_x, new_y)] = 0
                new_dots[(new_x, new_y)] += dots[dot]
            # Just keep at existing location
            else:
                if not new_dots.get(dot):
                    new_dots[dot] = 0
                new_dots[dot] += dots[dot]
        # Fake dot at y - 1
        if not new_dots.get((0, line_position - 1)):
            new_dots[(0, line_position - 1)] = 0
        dots = new_dots

    if direction == 'x':
        for dot in dots:
            dot_x = dot[0]
            dot_y = dot[1]
            if dot_x > line_position:
                # Move the dot up

                dif_x = dot_x - line_position
                new_x = line_position - dif_x
                new_y = dot_y
                if not new_dots.get((new_x, new_y)):
                    new_dots[(new_x, new_y)] = 0
                new_dots[(new_x, new_y)] += dots[dot]
            # Just keep at existing location
            else:
                if not new_dots.get(dot):
                    new_dots[dot] = 0
                new_dots[dot] += dots[dot]
        # Fake dot at x - 1
        if not new_dots.get((line_position - 1), 0):
            new_dots[(line_position - 1), 0] = 0
        dots = new_dots

    print(f'{dots=}')

    return dots

def display_dots(dots):
    max_x = max([x[0] for x in dots])
    max_y = max([y[1] for y in dots])

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if dots.get((x,y)):
                if dots[(x,y)] > 0:
                    print('8', end='')
                else:
                    print(' ',end='')
            else:
                print(' ', end='')
        print()


def count_dots(dots):
    dot_count = 0
    for dot in dots:
        if dots[dot] > 0:
            dot_count += 1

    return dot_count


def main():
    day = 13

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = fh.readlines()

    with open(f'input/day_{day:02d}.txt') as fh:
        data = fh.readlines()

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "single_small_cave": True,
            "assert_value": 17

        },
        {
            "name": "** Part 01 **",
            "data": data,

        },
        # {
        #     "name": "** Part 2 **",
        #     "data": data,
        #     "single_small_cave": False
        # },

    ]

    for run in runs:
        print(run['name'])

        dots, folds = parse_data(run['data'])

        # First fold
        dots = do_fold(dots, folds[0])
        dot_count = count_dots(dots)

        print(f'{dot_count=}')


        for fold in folds[1:]:
            dots = do_fold(dots, fold)
        display_dots(dots)





        #
        # if (av := run.get('assert_value')) is not None:
        #     if (n_routes != av):
        #         print(f"Error - expected {av=} got {n_routes=}")




if __name__ == "__main__":
    main()
