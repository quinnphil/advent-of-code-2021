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
    elif with_diagonal and abs(vent['x1'] - vent['x2']) == abs(vent['y1'] - vent['y2']):
        dx = int((vent['x2'] - vent['x1']) / abs(vent['x2'] - vent['x1']))
        dy = int((vent['y2'] - vent['y1']) / abs(vent['y2'] - vent['y1']))

    # Nothing to do
    else:
        return vent_points

    # Have directions, now just walk to next point
    ax = vent['x1']
    ay = vent['y1']
    vent_points.append((ax, ay))

    while ax != vent['x2'] or ay != vent['y2']:
        ax += dx
        ay += dy
        vent_points.append((ax, ay))

    return vent_points


def get_vent_map(vents, with_diagonal=False):
    vent_map = {}
    for vent in vents:
        vent_points = get_vent_points(vent, with_diagonal=with_diagonal)
        for vent_point in vent_points:
            if vent_point not in vent_map:
                vent_map[vent_point] = 0
            vent_map[vent_point] += 1
    return vent_map


def count_overlaps(map):
    overlaps = 0
    for p in map:
        if map[p] > 1:
            overlaps += 1
    return overlaps


def main():
    day = 5

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "with_diagonal": False,
            "assert_value": 5
        },
        {
            "name": "** Part 01 **",
            "data": data,
            "with_diagonal": False
        },
        {
            "name": "** Test 02 **",
            "data": data_test,
            "with_diagonal": True,
            "assert_value": 12
        },
        {
            "name": "** Part 02 **",
            "data": data,
            "with_diagonal": True
        }
    ]

    for run in runs:
        print(run['name'])
        vents = get_vents(run['data'])
        vent_map = get_vent_map(vents, with_diagonal=run['with_diagonal'])
        overlaps = count_overlaps(vent_map)
        print(f"{overlaps=}")
        if assert_value := run.get('assert_value'):
            assert (overlaps == assert_value)
        print()


if __name__ == "__main__":
    main()
