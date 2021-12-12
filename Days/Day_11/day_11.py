import utils

def make_grid(data):
    grid = {}

    for y, row in enumerate(data):
        for x, e in enumerate(row):
            grid[(y, x)] = int(e)

    return grid

def display_grid(grid):

    for y in range(0,10):
        print()
        for x in  range(0, 10):
            print(grid[(y, x)], end='')
    print()
    print()
    return grid

def count_flashes(grid):
    flash_count = 0
    flashed = set()
    in_sync = False
    queue = []

    # Update everything in grid
    for p in grid:
        grid[p] += 1
        queue.append(p)

    while queue:
        p = queue.pop(0)
        py = p[0]
        px = p[1]

        if grid[p] > 9 and p not in flashed:
            # Increment
            flash_count += 1
            # Add neighbours to queue
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                sy = py + dy
                sx = px + dx

                # Increment neighbour
                if grid.get((sy, sx)):
                    grid[(sy, sx)] += 1
                    queue.append((sy, sx))

                # Add to flashed
                flashed.add(p)
    print(f'{flashed=}')

    # Now reset anything greater than 9
    for p in grid:
        if grid[p] > 9:
            grid[p] = 0
    if len(flashed) == len(grid):
        in_sync = True

    return grid, flash_count, in_sync



def main():
    day = 11

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value_p1": 1656,
            "assert_value_p2": 195
        },
        {
            "name": "** Part 01 **",
            "data": data
        },
    ]

    for run in runs:
        print(run['name'])
        grid = make_grid(run['data'])

        flash_sum = 0

        print("START")
        display_grid(grid)

        for step in range (1, 101):

            grid, flash_count, _ = count_flashes(grid)
            flash_sum += flash_count
            print(f'{step} => {flash_count=}')
            display_grid(grid)

        in_sync = False
        step = 0
        flash_sum = 0

        grid = make_grid(run['data'])

        while not in_sync:
            step += 1
            queue = list(grid.keys())
            grid, flash_count, in_sync = count_flashes(grid)
            flash_sum += flash_count
            print(f'{step} => {flash_count=}')
            display_grid(grid)

        print(f'{step=}')

        # print(f'{grid=}')
        print(f'{flash_sum=}')
        # assert(flash_sum == 1656)



if __name__ == "__main__":
    main()
