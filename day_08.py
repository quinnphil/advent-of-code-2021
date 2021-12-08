import utils
import math
def get_digits():
    digits = dict()
    primes = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29
    }
    digits[0] = math.prod([primes[l] for l in "abcefg"])
    digits[1] = math.prod([primes[l] for l in "cf"])
    digits[2] = math.prod([primes[l] for l in "acdeg"])
    digits[3] = math.prod([primes[l] for l in "acdfg"])
    digits[4] = math.prod([primes[l] for l in "bcdf"])
    digits[5] = math.prod([primes[l] for l in "abdfg"])
    digits[6] = math.prod([primes[l] for l in "abdefg"])
    digits[7] = math.prod([primes[l] for l in "acf"])
    digits[8] = math.prod([primes[l] for l in "abcdefg"])
    digits[9] = math.prod([primes[l] for l in "abcdfg"])

    return digits



def get_lines(data):
    lines = []
    for i, line in enumerate(data):
        signal, output = line.split('|')
        signal = [s for s in signal.strip().split(' ')]
        output = [o for o in output.strip().split(' ')]
        lines.append({
            "line": i,
            "signals": signal,
            "output": output
        })
    return(lines)

def count_easy_digits(output):
    count = 0
    for l in output:
        for s in l:
            if len(s) in [2,3,4,7]:
                count+=1
    return(count)

def get_digit_mappings(signal, original_map):
    print(f"{original_map=}")

    digit_map = dict()
    for digit in signal:
        print(f"{digit=}")
        if len(digit) == 2:
            digit_map[1] = digit
        elif len(digit) == 3:
            digit_map[7] = digit
        elif len(digit) == 4:
            digit_map[4] = digit
        elif len(digit) == 7:
            digit_map[8] = digit

    primes = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29
    }

    # Setup all signal products
    # signal_products = dict()
    # for s in signal:
    #     signal_products[s] =  math.prod([primes[l] for l in s])

    letter_map = dict()
    A = ""
    B = ""
    C = ""
    D = ""
    E = ""
    F = ""
    G = ""

    # Set of letters in 7 / 1 = a prime in the original set
    digit_map[7]
    (A,) = (set(digit_map[7]) ^ set(digit_map[1]))
    print(A)
    letter_map[A] = primes['a']


    # If I multiple mapping 4 by prime['a'] and diff this with 9 I solve for G
    g_candidate = (digit_map[4] + A)
    g_candidate_product = math.prod([primes[l] for l in g_candidate])

    for s in signal:
        if len(g_candidate) >= len(s):
            continue
        set_diff = set(s) ^ set(g_candidate)
        if len(set_diff) == 1:
            (G,) = set_diff
            letter_map[G] = primes['g']
            digit_map[9] = s

    # Now solve for 8 by adding e to 9 - solves for e
    g_candidate = digit_map[9]
    for s in signal:
        if len(s) == 7:
            set_diff = set(s) ^ set(g_candidate)
            (E,) = set_diff
            letter_map[E] = primes['e']
            digit_map[8] = s

    # Solved for 3 & D
    # Taking A and G off 3 and len(2) for 1
    for s in signal:
        if len(s) == 5:
            print(s)
            set_diff = set(s) ^ set([A, G])
            set_diff = set_diff ^ set(digit_map[1])

            if len(set_diff) == 1:
                (D,) = set_diff
                letter_map[D] = primes['d']
                digit_map[3] = s



    # Remove D from 8 to solve for 0
    zero_str = digit_map[8].replace(D, '')
    print(f"{zero_str=}")
    for s in signal:
        if set(s) == set(zero_str) and len(s) == len(zero_str):
            digit_map[0] = s


    # 6 is the only remaining 1-gap number
    # find 6
    unsolved = set(signal) ^ set(digit_map.values())
    print(unsolved)
    for s in unsolved:
        if len(s) == 6:
            digit_map[6] = s


    # 6 - E is 5
    five = set(digit_map[6].replace(E, ''))
    unsolved = set(signal) ^ set(digit_map.values())
    for s in unsolved:
        if five == set(s) and len(five) == len(s):
            digit_map[5] = s
        else:
            digit_map[2] = s

    print(f"{A=}{B=}{C=}{D=}{E=}{F=}{G=}")
    print(f"{digit_map=}")
    print(f"{letter_map=}")


    return(digit_map)

def main():
    day = 8

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = utils.lines(fh.read())



    with open(f'input/day_{day:02d}.txt') as fh:
        data = utils.lines(fh.read())

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

    def get_number(output, digit_map):
        s_num = ''

        for o in output:
            for i in digit_map:
                set_m = set(digit_map[i])
                set_o = set(o)

                if (set_m == set_o) and (len(set_m) == len(set_o)):
                    s_num += str(i)
        num = int(s_num)
        return num

    for run in runs:
        print(run['name'])
        digits = get_digits()
        lines = get_lines(run['data'])

        output = [o['output'] for o in lines]
        easy_digits = count_easy_digits(output)

        print(f"{easy_digits=}")

        sum = 0
        for line in lines:
            signal = line['signals']
            digit_map = get_digit_mappings(signal, original_map=digits)
            num = get_number(line['output'], digit_map)
            sum += num

        print(sum)


if __name__ == "__main__":
    main()
