import utils
import math


def make_grid(data):
    grid = {}

    for y, row in enumerate(data):
        for x, e in enumerate(row):
            grid[(y, x)] = int(e)

    return grid


def get_lowpoints(grid):
    low_points = {}
    not_low_point = {}

    for p in grid:
        # Skip if not a low point
        if p in not_low_point.keys():
            continue
        py = p[0]
        px = p[1]
        pv = grid[p]

        siblings = {}
        # North, South, East, West
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            sy = py + dy
            sx = px + dx
            if (s := grid.get((sy, sx))) is not None:
                siblings[(sy, sx)] = s

        if all(sv > pv for sv in siblings.values()):
            # Found low point
            low_points[(py, px)] = pv
            # None of the siblings can be low points
            for sv in siblings:
                not_low_point[sv] = siblings[sv]

    return low_points


def get_basins(grid, low_points):

    basins = []

    # Deal with everything as a tuple -- this allows popping on/off
    # Also - I don't care about the value of the from this point onwards
    for low_point in low_points:
        p_queue = []
        p_done = []
        p_queue.append(low_point)

        while len(p_queue) > 0:
            p = p_queue.pop()
            py = p[0]
            px = p[1]
            pv = grid[p]

            # Skip if we've already been to this point
            # Also skip 9s
            if p in p_done or pv == 9:
                continue

            # North, South, East, West
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                sy = py + dy
                sx = px + dx
                if (s := grid.get((sy, sx))) is not None:
                    if (s >= pv) and (s < 9):
                        # check if already seen
                        if (sy, sx) not in p_done:
                            p_queue.append((sy, sx))
            p_done.append(p)
        basins.append(p_done)
    return basins


def main():
    day = 9

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 15,
            "assert_value2": 1134
        },
        {
            "name": "** Part 01 **",
            "data": data,

        },
    ]

    for run in runs:
        print(run['name'])

        grid = make_grid(run['data'])
        low_points = get_lowpoints(grid)
        print(f'{low_points}')

        risk = sum(low_points.values()) + len(low_points)
        print(f'{risk=}')

        basins = get_basins(grid, low_points)
        s_basins = sorted(basins, key=len, reverse=True)
        basin_product2 = math.prod([len(s) for s in s_basins[:3]])
        print(f'{basin_product2=}')


if __name__ == "__main__":
    main()
