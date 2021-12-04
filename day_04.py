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
        assert(len(numbers) == x_size * y_size)
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
    print(bingo_numbers)
    boards = []
    numbers = []
    for row in all_numbers[1:]:
        if row == "":
            print('blank')
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
    data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

    print('** Test **')
    bingo_numbers, boards = make_boards(data.splitlines())

    for bingo_number in bingo_numbers:
        print(f"Called {bingo_number}")
        for board in boards:
            board.call(bingo_number)
            is_bingo = board.check_bingo()

        if is_bingo:
            score = board.get_score()
            print(f"{score=}")
            break

    day = 4
    data = utils.lines(utils.read_input_file(day))
    bingo_numbers, boards = make_boards(data)

    # print('** Part 01 **')
    # is_bingo = False
    # for bingo_number in bingo_numbers:
    #     print(f"Called {bingo_number}")
    #     for i, board in enumerate(boards):
    #         board.call(bingo_number)
    #         is_bingo = board.check_bingo()
    #
    #         if is_bingo:
    #             print("-- BINGO -- ")
    #             score = board.get_score()
    #             print(f"{i=}")
    #             print(f"{board=}")
    #             print(f"{score=}")

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
