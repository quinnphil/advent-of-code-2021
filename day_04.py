import utils


class Square:
    def __init__(self, number):
        self.number = int(number)
        self.is_called = False

    def call(self):
        self.is_called = True

    def __repr__(self):
        return f"{self.number=} {self.is_called}"


class Board:
    def __init__(self, numbers, x_size=5, y_size=5):
        self.squares = []
        self.x_size = x_size
        self.y_size = y_size
        self.score = 0
        self.last_called = -1
        assert (len(numbers) == x_size * y_size)
        for x in range(x_size):
            self.squares.append([])
            for y in range(y_size):
                e = numbers.pop(0)
                self.squares[x].append(Square(e))

    def call(self, number):

        self.last_called = int(number)
        for x in range(self.x_size):
            for y in range(self.y_size):
                if self.squares[x][y].number == int(number):
                    self.squares[x][y].call()

    def check_bingo(self):
        # check columns:
        for x in range(self.x_size):
            marked = 0
            for y in range(self.y_size):
                if self.squares[x][y].is_called:
                    marked += 1
            if marked == self.x_size:
                return True
        # rows
        for y in range(self.y_size):
            marked = 0
            for x in range(self.x_size):
                if self.squares[x][y].is_called:
                    marked += 1

            if marked == self.y_size:
                return True
        return False

    def get_score(self):
        unmarked = []
        for x in range(self.x_size):
            for y in range(self.y_size):
                if not self.squares[x][y].is_called:
                    unmarked.append(int(self.squares[x][y].number))
        print(f"{self.last_called=}")
        print(f"{unmarked=}")
        self.score = sum(unmarked) * int(self.last_called)
        print(f"{self.score}")
        return self.score

    def __repr__(self):
        return str(self.squares)


def make_boards(data):
    all_numbers = data
    bingo_numbers = [int(n) for n in all_numbers[0].split(',')]

    boards = []
    numbers = []
    for row in all_numbers[1:]:
        if row == "":
            if len(numbers) > 0:
                board = Board(numbers)
                boards.append(board)
                numbers = []
        else:
            for n in (row.strip()).split(' '):
                if n == '' or n == ' ':
                    continue
                numbers.append(int(n))
    # Last row
    board = Board(numbers)
    boards.append(board)
    return (bingo_numbers, boards)


def main():
    day = 4

    with open (f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())


    print('** Test **')
    bingo_numbers, boards = make_boards(data_test)

    for bingo_number in bingo_numbers:
        print(f"Called {bingo_number}")
        for board in boards:
            board.call(bingo_number)
            is_bingo = board.check_bingo()

        if is_bingo:
            score = board.get_score()
            print(f"{score=}")
            break


    print('** Part 01 **')
    data = utils.lines(utils.read_input_file(day))
    bingo_numbers, boards = make_boards(data)

    is_bingo = False
    print("Calling numbers: ", end='')
    for bingo_number in bingo_numbers:
        print(f"{bingo_number}, ", end='')
        for i, board in enumerate(boards):
            board.call(bingo_number)
            is_bingo = board.check_bingo()

            if is_bingo:
                print("-- BINGO -- ")
                score = board.get_score()
                print(f"{i=}")
                print(f"{board=}")
                print(f"{score=}")
                break
        if is_bingo:
            break

    exit()

    print("Part 02")
    winning_order = []
    already_won = []
    for i, bingo_number in enumerate(bingo_numbers):
        print(f"Called {bingo_number}")
        for i, board in enumerate(boards):
            board.call(bingo_number)
            is_bingo = board.check_bingo()

            if is_bingo and i not in already_won:
                print("-- BINGO -- ")
                already_won.append(i)
                winning_order.append(board.get_score())
    print(f"{winning_order[-1]}")


if __name__ == "__main__":
    main()
