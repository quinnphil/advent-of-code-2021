import utils
from collections import Counter


def make_map(paths):
    cave_map = {}

    # Go through list making caves
    for path in paths:
        node_a, node_b = path.split('-')

        for start_node, end_node in [(node_a, node_b), (node_b, node_a)]:

            # Skip adding if end and start in wrong location
            if start_node == 'end' or end_node == 'start':
                continue
            else:
                if not cave_map.get(start_node):
                    cave_map[start_node] = []
                cave_map[start_node].append(end_node)

    return cave_map


def solve(cave_map, current_cave, route, routes, single_small_cave=True):
    # Success - End cave found
    if current_cave == 'end':
        route.append(current_cave)
        routes.append(route)
        return routes

    # Bad route - already been to this small cave
    if (current_cave.lower() == current_cave) and (current_cave in route):
        if single_small_cave:  # only one visit allowed
            route.append(current_cave)
            routes.append(route)
            return routes
        else:
            # Only a problem if any small cave has already been visited twice
            lower_caves = [x for x in route if x.lower() == x]
            lc_counts = Counter(lower_caves)
            if 2 in lc_counts.values():
                # already seen a cave twice
                return routes

    route.append(current_cave)
    for next_cave in cave_map[current_cave]:
        routes = solve(cave_map, next_cave, route.copy(), routes, single_small_cave)

    return routes


def walk_map(cave_map, single_small_cave):
    routes = solve(cave_map, "start", [], [], single_small_cave)

    good_routes = [route for route in routes if route[-1] == 'end']

    return good_routes


def main():
    day = 12

    with open(f'input/day_{day:02d}_test_01.txt') as fh:
        data_test_01 = utils.lines(fh.read())

    with open(f'input/day_{day:02d}_test_02.txt') as fh:
        data_test_02 = utils.lines(fh.read())

    with open(f'input/day_{day:02d}_test_03.txt') as fh:
        data_test_03 = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test_01,
            "single_small_cave": True,
            "assert_value": 10

        },
        {
            "name": "** Test 02 **",
            "data": data_test_02,
            "single_small_cave": True,
            "assert_value": 19

        },
        {
            "name": "** Test 03 **",
            "data": data_test_03,
            "single_small_cave": True,
            "assert_value": 226

        },
        {
            "name": "** Part 01 **",
            "data": data,
            "single_small_cave": True
        },
        {
            "name": "** Test 4 **",
            "data": data_test_02,
            "single_small_cave": False,
            "assert_value": 103
        },
        {
            "name": "** Part 2 **",
            "data": data,
            "single_small_cave": False
        },

    ]

    for run in runs:
        print(run['name'])

        cave_map = make_map(run['data'])
        routes = walk_map(cave_map, run['single_small_cave'])

        n_routes = len(routes)

        if (av := run.get('assert_value')) is not None:
            if (n_routes != av):
                print(f"Error - expected {av=} got {n_routes=}")

        print(f'{n_routes=}')


if __name__ == "__main__":
    main()
