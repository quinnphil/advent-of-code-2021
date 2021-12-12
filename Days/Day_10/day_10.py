import utils
import math
import re
from collections import deque

def check_lines(lines):
    chunk_sets = {
        '(': ')',
        '[': ']',
        '<': '>',
        '{': '}'
    }
    scores_corrupt = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    scores_incomplete = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    corrupt_lines = []
    incomplete_lines = []

    for l, line in enumerate(lines):
        stack = deque()
        expecting = []
        i = 0
        error = False

        while i < len(line) and not error:
            c = line[i]
            # Add open character to stack
            if c in chunk_sets:
                stack.append(c)
            else:
                # Check expected close character compliments last added open character
                last_c = stack.pop()

                if not chunk_sets[last_c] == c:
                    corrupt_line = (l, i, last_c, c, scores_corrupt[c])
                    corrupt_lines.append(corrupt_line)
                    error = True
            i += 1
        # Handle incomplete lines
        if not error:
            score = 0

            while stack:
                c = stack.pop()
                score = (score * 5) + scores_incomplete[chunk_sets[c]]
            incomplete_line = (l, i, score)
            incomplete_lines.append(incomplete_line)

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
            "assert_value_p1": 26397,
            "assert_value_p2": 288957
        },
        {
            "name": "** Part 01 **",
            "data": data
        },
    ]

    for run in runs:
        print(run['name'])

        corrupt_lines2, incomplete_lines = check_lines(run['data'])
        score = sum(s[4] for s in corrupt_lines2)

        if (av := run.get('assert_value_p1')) is not None:
            print(f'{score=} <=> {av=}')
            assert(score == av)

        print(f'{score=}')

        sorted_scores = sorted([s[2] for s in incomplete_lines])
        mid_point = int(len(sorted_scores) / 2)
        score_incomplete = sorted_scores[mid_point]
        if (av := run.get('assert_value_p2')) is not None:
            print(f'{score_incomplete=} <=> {av=}')
            assert(score_incomplete == av)
        print(f'{score_incomplete=}')


if __name__ == "__main__":
    main()
