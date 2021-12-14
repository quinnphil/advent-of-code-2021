import utils
from collections import Counter

def parse_data(data):
    print(f'{data=}')

    rules = {}
    template = data[0].strip()

    for line in data[2:]:
        p1, p2 = line.strip().split(' -> ')

        rules[p1] = p2

    return template, rules


def main():
    day = 14

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = fh.readlines()

    with open(f'input/day_{day:02d}.txt') as fh:
        data = fh.readlines()



    runs = [
        # {
        #     "name": "** Test 01 **",
        #     "data": data_test,
        #     "assert_value": 10
        #
        # },
        {
            "name": "** Part 01 **",
            "data": data,

        },


    ]

    for run in runs:
        print(run['name'])

        template, rules = parse_data(run['data'])

        print(f'{rules=}')
        print(f'{template=}')

        compounds = {}
        letters = {}

        # Initialise compounds with rules
        for r in rules:
            compounds[r] = 0

        # Initialise letters
        for l in template:
            if not letters.get(l):
                letters[l] = 0
            letters[l] += 1

        # Initialise compounds from template
        for i, c in enumerate(template[:-1]):
            s = template[i:i+2]
            if not compounds.get(s):
                compounds[s] = 0
            compounds[s] += 1

        print(f'{compounds=}')
        print(f'{letters=}')


        for step in range (1, 41):
            new_compounds = {}
            for old_c in compounds:
                if compounds[old_c] <= 0:
                    continue
                new_letter = rules[old_c]
                print(f'{step=} {old_c=} {new_letter=} {letters=}')
                print(f'{compounds=}')


                new_c1 = old_c[0] + new_letter
                new_c2 = new_letter + old_c[1]

                # Add letter if not there
                if not letters.get(new_letter):
                    letters[new_letter] = 0
                letters[new_letter] += compounds[old_c]

                if not new_compounds.get(new_c1):
                    new_compounds[new_c1] = 0
                new_compounds[new_c1] += compounds[old_c]


                if not new_compounds.get(new_c2):
                    new_compounds[new_c2] = 0
                new_compounds[new_c2] += compounds[old_c]

                # Set old compound to remove
                if not new_compounds.get(old_c):
                    new_compounds[old_c] = 0
                new_compounds[old_c] -= compounds[old_c]
            # Add new
            for new_c in new_compounds:
                compounds[new_c] += new_compounds[new_c]

        print(f'{letters=}')
        print(f'{compounds=}')


        element_counts = Counter(letters)
        print(f'{letters=}')


        most_common = element_counts.most_common()[0][1]
        least_common = element_counts.most_common()[-1][1]
        diff = most_common - least_common

        print(f'{most_common=}')
        print(f'{least_common=}')
        print(f'{diff=}')


        # if (av := run.get('assert_value')) is not None:
        #     if (n_routes != av):
        #         print(f"Error - expected {av=} got {n_routes=}")




if __name__ == "__main__":
    main()
