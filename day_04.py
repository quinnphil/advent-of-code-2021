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

        self.score = sum(unmarked) * int(self.last_called)
        return self.score

    def draw_board_state(self):
        board_pic = ""
        for x in range(self.x_size):
            for y in range(self.y_size):
                if self.squares[x][y].is_called:
                    board_pic += f"-- "
                else:
                    board_pic += f"{self.squares[x][y].number:02d} "
            if x < self.x_size - 1:
                board_pic += "\n"
        print(board_pic)


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

    print("Calling numbers: ", end='')
    for bingo_number in bingo_numbers:
        print(f"{bingo_number} ", end='')
        for i, board in enumerate(boards):
            # board.draw_board_state()
            board.call(bingo_number)
            is_bingo = board.check_bingo()

        if is_bingo:
            print("-- BINGO --")
            print(f"[Board {i}]")
            board.draw_board_state()
            score = board.get_score()
            print(f"{score=}")
            break
    print("-"*80)


    data = utils.lines(utils.read_input_file(day))
    bingo_numbers, boards = make_boards(data)

    winning_order = []
    already_won = []
    print("Calling numbers: ", end='')
    for i, bingo_number in enumerate(bingo_numbers):
        print(f"{bingo_number} ", end='')
        for j, board in enumerate(boards):
            if j in already_won:
                continue
            board.call(bingo_number)
            is_bingo = board.check_bingo()

            if is_bingo and j not in already_won:
                print("-- BINGO -- ")
                already_won.append(j)
                winning_order.append(board)
    print("\n")
    print("-" * 80)

    print('** Part 01 **')
    first_winner = winning_order[0]
    first_winner_board_num = already_won[0]

    print(f"[Board {first_winner_board_num}]")
    first_winner.draw_board_state()
    score = first_winner.get_score()
    print(f"{score=}")

    print("-" * 80)
    print('** Part 02 **')
    last_winner = winning_order[-1]
    last_winner_board_num = already_won[-1]

    print(f"[Board {last_winner_board_num}]")
    last_winner.draw_board_state()
    score = last_winner.get_score()
    print(f"{score=}")


if __name__ == "__main__":
    main()
