
def read_input_file(day:int):
    with open(f'input/day_{day:02d}.txt') as f:
        return f.read()

def lines(input):
    return list(input.splitlines())

def ints(input):
    return list(map(int, input))

