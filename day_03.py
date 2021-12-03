import utils


def get_bit_counts(byte_list):
    byte_length = len(byte_list[0])
    bit_counts = [0] * byte_length
    for byte in byte_list:
        for i, bit in enumerate(byte):
            bit_counts[i] += int(bit)
    return bit_counts


def get_power_consumption(byte_list):
    byte_length = len(byte_list[0])
    list_length = len(byte_list)

    bit_counts = get_bit_counts(byte_list)

    gamma_c = [0] * byte_length
    epsilon_c = [0] * byte_length
    for i, bit_c in enumerate(bit_counts):
        if bit_c >= (list_length) / 2:
            gamma_c[i] = 1
            epsilon_c[i] = 0
        else:
            gamma_c[i] = 0
            epsilon_c[i] = 1

    gamma = int(''.join(str(e) for e in gamma_c), 2)
    epsilon = int(''.join(str(e) for e in epsilon_c), 2)
    power_consumption = gamma * epsilon
    print(f"{gamma=}")
    print(f"{epsilon=}")
    print(f"{power_consumption=}")
    return power_consumption


def get_gas_rating(start_bit, pos, byte_list, bit_counts):
    new_list = []

    if bit_counts[pos] >= (len(byte_list) / 2):
        keep = start_bit
    else:
        keep = not start_bit

    for byte in byte_list:

        if int(byte[pos]) == keep:
            new_list.append(byte)

    if len(new_list) > 1:
        pos += 1
        bit_counts = get_bit_counts(new_list)

        new_list = get_gas_rating(start_bit, pos, new_list, bit_counts)
    else:
        return new_list[0]

    return new_list


def get_life_support_rating(byte_list):
    bit_counts = get_bit_counts(byte_list)

    o2_generator_rating = get_gas_rating(True, 0, byte_list, bit_counts)
    o2_generator_rating = int(o2_generator_rating, 2)
    print(f"{o2_generator_rating=}")

    co2_scrubber_rating = get_gas_rating(False, 0, byte_list, bit_counts)
    co2_scrubber_rating = int(co2_scrubber_rating, 2)
    print(f"{co2_scrubber_rating=}")

    life_support_rating = o2_generator_rating * co2_scrubber_rating
    print(f"{life_support_rating=}")
    return life_support_rating


def main():
    print('** Test 01 **')
    bit_list = ("00100\n"
                "11110\n"
                "10110\n"
                "10111\n"
                "10101\n"
                "01111\n"
                "00111\n"
                "11100\n"
                "10000\n"
                "11001\n"
                "00010\n"
                "01010")
    print(get_power_consumption(bit_list.splitlines()))
    print()

    day = 3
    data = utils.lines(utils.read_input_file(day))

    print('** Part 01 **')
    print(get_power_consumption(data))
    print()

    print('** Test 02 **')
    print(get_life_support_rating(bit_list.splitlines()))
    print()

    print('** Part 02 **')
    print(get_life_support_rating(data))
    print()


if __name__ == "__main__":
    main()
