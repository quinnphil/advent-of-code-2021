import utils

def get_vents(data):
    vents = []
    for line in data:
        pairs = line.split(' -> ')
        x1, y1 = pairs[0].split(',')
        x2, y2 = pairs[1].split(',')
        vents.append({
            "x1": int(x1),
            "y1": int(y1),
            "x2": int(x2),
            "y2": int(y2)
        })

    return vents


def get_vent_points(vent, with_diagonal=False):
    vent_points = []

    # Horizontal
    if vent['y1'] == vent['y2']:
        dx = int((vent['x2'] - vent['x1']) / abs(vent['x2'] - vent['x1']))
        dy = 0

    # Vertical
    elif vent['x1'] == vent['x2']:
        dy = int((vent['y2'] - vent['y1']) / abs(vent['y2'] - vent['y1']))
        dx = 0

    # Diagonal
    elif with_diagonal and abs(vent['x1'] - vent['x2']) == abs(vent['x1'] - vent['x2']):
        dx = int((vent['x2'] - vent['x1']) / abs(vent['x2'] - vent['x1']))
        dy = int((vent['y2'] - vent['y1']) / abs(vent['y2'] - vent['y1']))

    # Nothing to do
    else:
        return vent_points

    # Have directions, now just walk to next point
    ax = vent['x1']
    ay = vent['y1']
    vent_points.append((ax, ay))

    while (ax != vent['x2'] or ay != vent['y2']):
        ax += dx
        ay += dy
        vent_points.append((ax, ay))

    return vent_points

def get_map(vents, with_diagonal=False):
    vent_locations = {}
    for vent in vents:
        vent_points = get_vent_points(vent, with_diagonal=with_diagonal)
        for vent_point in vent_points:
            if vent_point not in vent_locations:
                vent_locations[vent_point] = 0
            vent_locations[vent_point] += 1
    return vent_locations


def count_overlaps(map):
    overlaps = 0
    for p in map:
        if map[p] > 1:
            overlaps += 1

    return overlaps


def main():
    day = 5

    with open (f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    print('** Test 01 **')
    vents = get_vents(data_test)
    map = get_map(vents)
    overlaps = count_overlaps(map)
    print(f"{overlaps=}")

    with open (f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())
    vents = get_vents(data)
    print('** Part 01 **')
    map = get_map(vents)

    overlaps = count_overlaps(map)
    print(f"{overlaps=}")

    print("-" * 80)

    print('** Test 02 **')
    vents = get_vents(data_test)
    map = get_map(vents, with_diagonal=True)
    overlaps = count_overlaps(map)
    print(f"{overlaps=}")

    print('** Part 02 **')
    vents = get_vents(data)
    map2 = get_map(vents, with_diagonal=True)
    overlaps = count_overlaps(map2)
    print(f"{overlaps=}")

if __name__ == "__main__":
    main()
