import utils
from collections import Counter


def make_map(paths):
    cave_map = {}

    # Go through list making caves
    for path in paths:
        start_node, end_node = path.split('-')

        # Get start and end nodes the right way round
        if end_node == 'start' or start_node == 'end':
            tmp_node = start_node
            start_node = end_node
            end_node = tmp_node

        if not cave_map.get(start_node):
            cave_map[start_node] = []
        cave_map[start_node].append(end_node)

        # Add way back
        if end_node != 'end' and start_node != 'start':
            if not cave_map.get(end_node):
                cave_map[end_node] = []
            cave_map[end_node].append(start_node)

    return cave_map

def solve(cave_map, current_cave, route, routes, single_small_cave=True):


    # Success - End cave found
    if current_cave == 'end':
        route.append(current_cave)
        routes.append(route)
        return routes

    # Bad route - already been to this small cave
    if (current_cave.lower() == current_cave) and (current_cave in route):
        if not single_small_cave:  # only one visit allowed
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


def walk_map(cave_map):
    routes = solve(cave_map, "start", [], [])

    print(f'{routes=}')
    print(f'{cave_map=}')

    good_routes = [route for route in routes if route[-1] == 'end']

    return good_routes



def main():
    day = 12

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        # {
        #     "name": "** Test 01 **",
        #     "data": data_test,
        #     "single_small_cave": True
        #
        # },
        {
            "name": "** Part 01 **",
            "data": data,
            "single_small_cave": True
        },
    ]

    for run in runs:
        print(run['name'])

        cave_map = make_map(run['data'])
        print(f'{cave_map=}')
        routes = walk_map(cave_map)

        print(f'{len(routes)=}')





if __name__ == "__main__":
    main()
