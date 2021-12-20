import heapq

def get_adjacent_points(data, x, y):
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1, y1 = x + dy, y + dx
        # If within bounds yield coordinate
        if 0 <= x1 < len(data) and 0 <= y1 < len(data[0]):
            yield x1, y1


def find_lowest_risk(grid, width, height):

    # It costs nothing to be at 0, 0
    pqueue = [(0, (0, 0))]

    # Visited 0, 0
    visited = {(0, 0)}

    while pqueue:
        # Get smallest item on heap (always the root)
        distance, (x, y) = heapq.heappop(pqueue)

        # Check is the last position if yes, return the distance
        if (x == height - 1) and (y == width - 1):
            return distance

        # Otherwise check adjacent points
        for x1, y1 in get_adjacent_points(grid, x, y):
            # If not visited
            if (x1, y1) not in visited:
                # Cost equals current distance + new distance
                heapq.heappush(pqueue, (distance + grid[x1][y1], (x1, y1)))
                visited.add((x1, y1))

def main():
    day = 15

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [[int(x) for x in line] for line in fh.read().splitlines()]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [[int(x) for x in line] for line in fh.read().splitlines()]



    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 10

        },
        {
            "name": "** Prod **",
            "data": data,

        },


    ]



    for run in runs:

        print(run['name'])
        width = len(run['data'][0])
        height = len(run['data'])

        print(f'{width=}')
        print(f'{height=}')

        risk = find_lowest_risk(run['data'], width, height)

        print(f'{risk=}')

        new_grid = [line * 5 for line in run['data'] * 5]
        for x in range(height * 5):
            for y in range(width * 5):

                old_v = new_grid[x][y]
                new_v = old_v + (x // height) + (y // width) - 1 # Compensate to keep first tile the same
                new_v = new_v % 9 + 1   # Increment and wrap
                new_grid[x][y] = new_v


        print(find_lowest_risk(new_grid, width * 5, height * 5))



if __name__ == "__main__":
    main()







