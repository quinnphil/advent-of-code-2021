import re
from bitstring import BitArray, BitStream
import binascii
from math import prod

def bin_to_int(binary):
    i = int(binary)
    return i

def read_header(bits):
    version = bits.read('uint:3')
    type_id = bits.read('uint:3')

    return version, type_id

def read_value(bits):
    n = BitArray()
    lead = b'1'
    while lead:
        lead = bits.read(1)
        n_bits = bits.read(4)
        n.append(n_bits)
        print(f'{lead=}')
        print(f'{n_bits=}')
        print(f'{n=}')
        print(f'{n.uint=}')


    return n.uint

# def get_packets(bits, packets):
#
#     version, type_id = read_header(bits)
#     packet = {
#         'type_id': type_id,
#         'version': version
#     }
#
#     ### Literal value
#     if type_id == 4:
#         value = read_value(bits)
#
#         packet['value'] = value
#         packets.append(packet)
#         return packets
#     ### Operator packet
#     else:
#         length_type_id = bits.read("uint:1")
#         # Read by length
#         if length_type_id == 0:
#             sp_total_bit_length = bits.read("uint:15")
#             c_pos = bits.pos
#             while bits.pos < c_pos + sp_total_bit_length:
#                 print(f'{sp_total_bit_length=}')
#                 print(f'{c_pos=}')
#                 print(f'{bits.pos=}')
#                 packets = get_packets(bits, packets)
#
#             print(f'{sp_total_bit_length=}')
#         # Read by packet count
#         else:
#             # read subpackets by count
#             sp_total_packets = bits.read("uint:11")
#             p_count = 0
#             while p_count < sp_total_packets:
#                 packets = get_packets(bits, packets)
#                 p_count += 1
#             print(f'{sp_total_packets=}')
#
#
#
#
#
#     packets.append(packet)
#     return packets

def get_packets(bits, val):

    version, type_id = read_header(bits)

    ### Literal value
    if type_id == 4:
        value = read_value(bits)
        return value

    ### Operator packet
    else:
        values = []
        length_type_id = bits.read("uint:1")
        # Read by length
        if length_type_id == 0:
            sp_total_bit_length = bits.read("uint:15")
            c_pos = bits.pos
            while bits.pos < c_pos + sp_total_bit_length:
                value = get_packets(bits,  val)
                values.append(value)

            print(f'{sp_total_bit_length=}')

        # Read by packet count
        else:
            # read subpackets by count
            sp_total_packets = bits.read("uint:11")
            values = []
            p_count = 0
            while p_count < sp_total_packets:
                value = get_packets(bits,  val)
                values.append(value)
                p_count += 1
            print(f'{sp_total_packets=}')
        print(f'{values=}')
        if type_id == 0:
            return sum(values)
        elif type_id == 1:
            return prod(values)
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            if values[0] > values[1]:
                return 1
            else:
                return 0
        elif type_id == 6:
            if values[0] < values[1]:
                return 1
            else:
                return 0
        elif type_id == 7:
            if values[0] == values[1]:
                return 1
            else:
                return 0



    return val


def sum_versions(packets):
    sv = 0

    for packet in packets:
        if version := packet.get('version'):
            sv += version

    return sv

def main():
    day = 16

    with open(f'input/day_{day:02d}_test.txt') as fh:
        data_test = fh.read()

    with open(f'input/day_{day:02d}.txt') as fh:
        data = fh.read()



    runs = [
        {
            "name": "** Test 01 **",
            "data": data_test,
            "assert_value": 10

        },
        {
            "name": "** Part 01 **",
            "data": data,

        },


    ]




    for run in runs:

        print(run['name'])
        print(run['data'])

        # input = binascii.unhexlify(run['data'])
        input = bytes.fromhex(run['data'])
        print(f'{input}')

        bits = BitStream(input)

        total = get_packets(bits, 0)
        print(f'{total=}')

        # print(packets)
        # # P1
        # sv = sum_versions(packets)
        # print(f'{sv=}')



if __name__ == "__main__":
    main()







