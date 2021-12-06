import utils
import json

class Fish():
    def __init__(self, timer):
        if timer:
            self.timer = timer
            self.is_new_fish = False

        else:
            self.timer = 8
            self.is_new_fish = True

    def pass_day(self):
        if self.is_new_fish:
            self.is_new_fish = False
            return False

        new_fish = False

        self.timer = self.timer - 1

        if self.timer == -1:
            new_fish = True
            self.timer = 6
        return new_fish

    def __repr__(self):
        return str(self.timer)


def simulate_fish(input, days):
    school = {i:0 for i in range(0, 9)}
    for f in input:
        if not school[f]:
            school[f] = 1
        else:
            school[f] += 1

    new_fish = 0


    for day in range(days):
        new_school = {i: 0 for i in range(0, 9)}
        respawn = 0
        new_fish = 0
        for f in school:
            if f == 0 and school[f] > 0:
                new_fish = school[0]
                respawn = school[0]
                school[0] = 0
            elif f <= 0:
                pass
            else:
                new_school[f-1] = school[f]
        new_school[6] += respawn
        new_school[8] += new_fish
        school = dict(new_school)
        # print(json.dumps(school, indent=2))
        fish_count = (sum(school.values()))
        # print(fish_count)


    return fish_count

def main():
    day = 6

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [int(f) for f in utils.lines(fh.read())[0].split(',')]

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "days": 80,
            "assert_value": 5934
        },
        {
            "name": "** Part 01 **",
            "data": data,
            "days": 80
        },
        {
            "name": "** Test 02 **",
            "data": data_test,
            "days": 256,
            "assert_value": 26984457539
        },
        {
            "name": "** Part 02 **",
            "data": data,
            "days": 256
        }
    ]

    for run in runs:
        print(run['name'])
        print(data)
        fish_count = simulate_fish(run['data'], run['days'])

        print(fish_count)
        if assert_value := run.get('assert_value'):
            assert (fish_count == assert_value)


if __name__ == "__main__":
    main()
