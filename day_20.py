from bitstring import BitArray, BitStream
from math import floor
from collections import deque

def parse_data(data):
    algorithm_chars, image_lines = data.split('\n\n')
    image_lines = image_lines.split('\n')

    image = {}
    algorithm = {}
    width = max(len(il) for il in image_lines)
    height = len(image_lines)


    # Algorithm
    for i, char in enumerate(algorithm_chars, 0):
        if char == "#":
            algorithm[i] = 1
        else:
            algorithm[i] = 0

    # Build image
    for y, image_line in enumerate(image_lines, - floor(height / 2)):
        for x, char in enumerate(image_line, - floor(width / 2)):
            if char == "#":
                image[x, - y] = 1
            else:
                image[x, - y] = 0
    return image, algorithm

def get_size(image):
    width = max([abs(p[0]) for p in image]) * 2
    height = max([abs(p[1]) for p in image]) * 2

    return width, height

def draw_image(image):
    print("--- Image ---")
    width, height = get_size(image)
    # for y in range(- floor(height / 2), floor(height / 2) + 1):
    #     for x in range (- floor(width / 2), floor(width / 2) + 1 ):
    for y in range(- floor(height / 2) - 1, floor(height / 2) + 2):
        for x in range (- floor(width / 2) - 1, floor(width / 2)  + 2 ):
            if image.get((x,-y)):
                print('#', end='')
            else:
                print('.', end='')
        print()

def get_neighbours(point):
    px, py = point
    neighbours = []
    for dx, dy in [(-1, 1), (0, 1), (1, 1), (-1,0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
        neighbours.append((px + dx, py + dy))

    return neighbours

def get_number_from_neighbours(image, neighbours, inf):
    bn = ""
    for p in neighbours:
        if (c:= image.get(p)) is not None:
            if c == 1:
                bn += "1"
            else:
                bn += "0"
        else:
            bn += inf
    n = int(bn, 2)
    return n





def enhance_image(image, algorithm, inf):

    queue = deque(image)
    new_image = {}

    while queue:

        point = queue.pop()
        if point in new_image:
            continue
        neighbours = get_neighbours(point)
        num = get_number_from_neighbours(image, neighbours,inf)

        # Update point
        new_image[point] = algorithm[num]


        # Add any neighbours to new image
        for neighbour in neighbours:
            if point in image and neighbour not in image:
                queue.append(neighbour)


    return new_image



def count_pixels(image):
    return sum(image.values())

def main():
    day = 20

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = fh.read()

    with open(f'input/day_{day:02d}.txt') as fh:
        data = fh.read()



    runs = [
        # {
        #     "name": "** Test 01 **",
        #     "data": data_test,
        #     "assert_value": 10
        #
        # },
        {
            "name": "** Part 01 **",
            "data": data,

        },


    ]




    for run in runs:

        print(run['name'])

        image, algorithm = parse_data(run['data'])


        # draw_image(image)
        for i in range (1, 51):
            print(f'{i=}')
            if i % 2 == 1:
                inf = "0"
            else:
                inf = "1"

            image = enhance_image(image, algorithm, inf)

        pixel_count = count_pixels(image)
        print(f'{pixel_count=}')



# 20474 too high


if __name__ == "__main__":
    main()