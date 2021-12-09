import utils
import math

def make_grid(data):
    width = max(len(d) for d in data)
    height = len(data)
    grid = [[-1] * width for i in range(height)]

    for y, row in enumerate(data):
        for x, element in enumerate(row):
            grid[y][x] = int(element)


    return grid



def get_lowpoints(grid):
    width = max(len(d) for d in grid)
    height = len(grid)

    low_points = []

    for y in range(0, height):
        for x in range(0, width):
            element = grid[y][x]
            local_points = []
            for dx in [-1, 1]:
                dy = 0
                if (x + dx) < 0 or (x + dx) >= width:
                    continue
                p = grid[y + dy][x + dx]
                local_points.append(p)
            for dy in [-1, 1]:
                dx = 0
                if (y+ dy) < 0 or (y + dy) >= height:
                    continue
                p = grid[y + dy][x + dx]
                local_points.append(p)
            if element < min(local_points):
                low_points.append((y,x,element))
    print(f"{low_points=}")


    return low_points




def get_risk(low_points):
    risk = 0
    for lp in low_points:
        risk += 1 + lp[2]

    print(f"{risk=}")
    return risk


def get_basins(grid,low_points):
    basins = []

    width = max(len(d) for d in grid)
    height = len(grid)

    for low_point in low_points:
        p_queue = []
        p_done = []
        p_queue.append(low_point)

        while len(p_queue) > 0:
            p = p_queue.pop()

            # Skip if we've already been to this basin
            # Also skip 9s
            if p in p_done or p[2] == 9:
                continue

            # Check adjacent horizontal
            for dx in [-1, 1]:
                cy = p[0]
                cx = p[1] + dx
                # Check x bounds
                if (cx < 0) or (cx >= width):
                    continue
                c = grid[cy][cx]
                # if (c == p[2]) or (c == p[2] + 1):
                if (c >= p[2]) and (c < 9):
                    # check if already seen
                    if (cy, cx, c) not in p_done:
                        p_queue.append((cy,cx, c))

            # Check adjacent vertical
            for dy in [-1, 1]:
                cx = p[1]
                cy = p[0] + dy
                # Check x bounds
                if cy < 0 or (cy >= height):
                    continue
                c = grid[cy][cx]
                # In range
                # if (c == p[2]) or (c == p[2] + 1):
                if (c >= p[2]) and (c < 9):
                    # check if already seen
                    if (cy, cx, c) not in p_done:
                        p_queue.append((cy, cx, c))
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

        risk = get_risk(low_points)
        if assert_value := run.get('assert_value'):
            assert (risk == assert_value)

        basins = get_basins(grid, low_points)

        s_basins = sorted( basins, key=len, reverse=True )
        basin_product = math.prod([len(s) for s in s_basins[:3]])
        print(f"{basin_product=}")



if __name__ == "__main__":
    main()
