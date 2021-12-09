import utils


class BasicSub:
    def __init__(self):
        self.x = 0
        self.y = 0

    def command(self, command):
        direction, units = command.split(' ')
        units = int(units)

        if direction == "forward":
            self.forward(units)
        elif direction == "up":
            self.up(units)
        elif direction == "down":
            self.down(units)

    def forward(self, units):
        self.x += units

    def down(self, units):
        self.y += units

    def up(self, units):
        self.y -= units

    def position(self):
        return self.x * self.y

    def __repr__(self):
        repr = f"""{self.x=}\n{self.y=}\n{self.position()=}"""
        return repr


class Submarine(BasicSub):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, units):
        self.x += units
        self.y += self.aim * units

    def down(self, units):
        self.aim += units

    def up(self, units):
        self.aim -= units

    def __repr__(self):
        repr = f"""{self.x=}\n{self.y=}\n{self.aim=}\n{self.position()=}"""
        return repr


def main():
    day = 2
    data = utils.lines(utils.read_input_file(day))

    commands_test = ("forward 5\n"
                     "down 5\n"
                     "forward 8\n"
                     "up 3\n"
                     "down 8\n"
                     "forward 2")

    print('** Test **')  # 150
    sub_test = BasicSub()
    for command in commands_test.splitlines():
        sub_test.command(command)
    print(f"{sub_test.position()=}")
    print()

    print('** Part 01 **')  # 1693300
    sub_p1 = BasicSub()
    for command in data:
        sub_p1.command(command)
    print(f"{sub_p1.position()=}")
    print()

    print('** Part 02 **')  # 1857958050
    sub_p2 = Submarine()
    for command in data:
        sub_p2.command(command)
    print(f"{sub_p2.position()=}")


if __name__ == "__main__":
    main()
