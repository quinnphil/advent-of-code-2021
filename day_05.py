import utils


class Square:
    def __init__(self, number):
        self.number = int(number)
        self.is_called = False

class Board:
    def __init__(self, numbers, x_size=5, y_size=5):
        self.squares = []
        self.x_size = x_size

    def __repr__(self):
        return str(self.squares)


def make_boards(data):
    all_numbers = data


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

def get_map(vents):
    max_x = max([v['x1'] for v in vents] + [v['x2'] for v in vents])
    max_y = max([v['y1'] for v in vents] + [v['y2'] for v in vents])
    map = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

    for vent in vents:
        # Horizontal
        if vent['x1'] == vent['x2']:
            x = vent['x1']
            y_min = min(vent['y1'], vent['y2'])
            y_max = max(vent['y1'], vent['y2'])
            for y in range (y_min, y_max + 1):
                map[y][x] += 1
        # Vertical
        if vent['y1'] == vent['y2']:
            y = vent['y1']
            x_min = min(vent['x1'], vent['x2'])
            x_max = max(vent['x1'], vent['x2'])
            for x in range(x_min, x_max + 1):
                map[y][x] += 1
    return map

def get_map2(vents):
    max_x = max([v['x1'] for v in vents] + [v['x2'] for v in vents])
    max_y = max([v['y1'] for v in vents] + [v['y2'] for v in vents])
    map = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

    for vent in vents:
        found = False
        # Horizontal
        if vent['x1'] == vent['x2']:
            x = vent['x1']
            y_min = min(vent['y1'], vent['y2'])
            y_max = max(vent['y1'], vent['y2'])
            for y in range (y_min, y_max + 1):
                map[y][x] += 1
                found = True
        # Vertical
        if vent['y1'] == vent['y2']:
            y = vent['y1']
            x_min = min(vent['x1'], vent['x2'])
            x_max = max(vent['x1'], vent['x2'])
            for x in range(x_min, x_max + 1):
                map[y][x] += 1
                found = True

        # Diagonal
        x_d = vent['x1'] - vent['x2']
        y_d = vent['y1'] - vent['y2']
        if not found and abs(x_d) == abs(y_d):
            # Take first point and walk in direction of second
            ax = vent['x1']
            ay = vent['y1']
            map[ay][ax] += 1
            while ax != vent['x2'] or ay != vent['y2']:
                if ax < vent['x2']:
                    ax += 1
                elif ax > vent['x2']:
                    ax -= 1
                if ay < vent['y2']:
                    ay += 1
                elif ay > vent['y2']:
                    ay -= 1
                map[ay][ax] += 1




    return map

def display_map(map):
    for x in map:
        for y in x:
            print(f"{y:02d} ", end='')
        print("\n")

def count_overlaps(map):
    overlaps = 0
    for x in map:
        for y in x:
            if y > 1:
                overlaps += 1

    return overlaps


def main():
    day = 5

    with open (f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    print('** Test 01 **')
    vents = get_vents(data_test)
    map = get_map(vents)
    # display_map(map)
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
    map = get_map2(vents)
    overlaps = count_overlaps(map)
    print(f"{overlaps=}")

    print('** Part 02 **')
    vents = get_vents(data)
    map2 = get_map2(vents)
    overlaps = count_overlaps(map2)
    print(f"{overlaps=}")

if __name__ == "__main__":
    main()
