import utils

def get_codes_by_len(codes):
    code_count = {}
    for code in codes:
        if not code_count.get(len(code)):
            code_count[len(code)] = []
        code_count[len(code)].append(code)

    return code_count

def decode_line(input, output):

    value = 0
    n = {}

    input_count = get_codes_by_len(input)


    # Easy numbers
    n[1] = input_count[2].pop()  # 1 is the only number with two segments
    n[4] = input_count[4].pop()   # 4 is the only number with four segments
    n[7] = input_count[3].pop()   # 7 is the only number with three segments
    n[8] = input_count[7].pop()   # 8 is the only number with seven segments

    # Solve
    # 9 minus 4 has a segment length of 2
    n[9] = [c for c in input_count[6] if len(set(c) ^ set(n[4])) == 2].pop()

    # 3 add 1 has segment length of 5
    n[3] = [c for c in input_count[5] if len(set(c) | set(n[1])) == 5].pop()

    # 6 add 1 has segment length of 7
    n[6] = [c for c in input_count[6] if len(set(c) | set(n[1])) == 7].pop()

    # 0 is the only other 6 length
    n[0] = [c for c in input_count[6] if c not in [n[6], n[9]]].pop()

    # 5 minus 6 has a segment length of 1
    n[5] = [c for c in input_count[5] if len(set(c) ^ set(n[6])) == 1].pop()

    # 2 is the only remaining 5 length
    n[2] = [c for c in input_count[5] if c not in [n[3], n[5]]].pop()

    nl = {''.join(sorted(v)): k for k, v in n.items()}

    str_int = ""
    for d in output:
        str_int += str(nl[''.join(sorted(d))])
    value = int(str_int)

    return value


def main():
    day = 8

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = [line for line in utils.lines(fh.read())]

    with open(f'input/day_{day:02d}.txt') as fh:
        data = [line for line in utils.lines(fh.read())]

        runs = [
            {
                "name": "** Test 01 **",
                "data": data_test,
                "assert_value": 26
            },
            {
                "name": "** Main **",
                "data": data

            },

        ]
#
    for run in runs:
        print(run['name'])

        lines = run['data']

        easy_digit_count = 0
        output_sum = 0
        for line in lines:
            input, output = [x.strip().split(' ') for x in line.split('|')]

            output_code_counts = get_codes_by_len(output)
            easy_digit_count += sum([len(output_code_counts[i]) for i in output_code_counts if i in (2,3,4,7)])

            output_value = decode_line(input, output)
            output_sum += output_value
        print(f'{easy_digit_count=}')
        print(f'{output_sum=}')


if __name__ == "__main__":
    main()
