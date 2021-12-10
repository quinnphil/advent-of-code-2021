import utils
import math
import re

def check_lines(lines):
    open = {
        '(': ')',
        '[': ']',
        '<': '>',
        '{': '}'
    }
    scores = {
        ')': 3,
        ']': 57,
        '>': 1197,
        '}': 25137
    }

    corrupt_lines = []


    for l, line in enumerate(lines):
        expecting = []
        i = 0
        error = False

        while i < len(line) and not error:
            c=line[i]
            next_close = None
            if expecting:
                next_close = expecting[-1]
            next_valid = list(open.keys())
            next_valid.append(next_close)

            if  (c in open.keys()):

                expecting.append(open[c])
            elif c == next_close:
                    expecting = expecting[:-1]
            else:
                error = True
                corrupt_lines.append((l, i, next_close, c, scores[c]))

            i+=1

    return corrupt_lines

def check_lines2(lines):
    open = {
        '(': ')',
        '[': ']',
        '<': '>',
        '{': '}'
    }
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    corrupt_lines = []
    incomplete_lines = []

    for l, line in enumerate(lines):
        scan = True
        i = 0
        old = line
        new = ""
        while scan:

            new = re.sub(r'(\[\])|(\{\})|(\(\))|(\<\>)','', old)

            # print(f'{old=}')
            # print(f'{new=}')

            # Basic string found
            if len(old) == len(new):
                scan = False
            else:
                old = new

        corrupt_line = None
        while not corrupt_line and i < len(new):
            c = new[i]
            if c in open.values():
                corrupt_line = (l, i, None, c, scores[c], new)

            i +=1
        if corrupt_line:
            corrupt_lines.append(corrupt_line)
        else:
            # Line is could be incomplete
            r_line = ""
            scores = {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
            }
            score = 0
            for c in new[::-1]:
                r_line += open[c]
                score = (score * 5) + scores[open[c]]

            print(f'{new=}')
            print(f'{r_line=}')
            print(f'{score=}')
            incomplete_line = (l, i, None, score, new, r_line)
            incomplete_lines.append(incomplete_line)
        # print(corrupt_lines)

    return corrupt_lines, incomplete_lines




def main():
    day = 10

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())

    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 26397
        },
        {
            "name": "** Part 01 **",
            "data": data,

        },
    ]

    for run in runs:
        print(run['name'])

        corrupt_lines2, incomplete_lines = check_lines2(run['data'])
        score = sum(s[4] for s in corrupt_lines2)


        print(f'{score=}')


        sorted_scores = sorted([s[3] for s in incomplete_lines])
        mid_point = int(len(sorted_scores) / 2)
        print(f'{sorted_scores=}')
        print(f'{mid_point=}')
        print(f'{sorted_scores[mid_point]=}')


        # 267657 Not this
        # 440013 == too high



if __name__ == "__main__":
    main()
