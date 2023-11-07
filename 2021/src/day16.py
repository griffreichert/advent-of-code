import utils

lines = utils.read_list(__file__, as_str=True)

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

# lines = ["9C0141080250320F1802104A08"]
packet = "".join(hex_to_binary[char] for char in lines[0])


def p1(packet):
    if all(char == "0" for char in packet) or len(packet) < 7:
        return 0

    version = int(packet[:3], 2)
    id_type = packet[3:6]

    # literal - base case
    if id_type == "100":
        i = 6
        literal = ""
        while packet[i] == "1":
            literal += packet[i + 1 : i + 5]
            i += 5
        literal += packet[i + 1 : i + 5]
        i += 5
        return version + p1(packet[i:])

    # operator - recursive
    else:
        # type length id
        type_len_id = packet[6]
        i = 7
        # number of sub packets
        if type_len_id == "1":
            operator_len = 11
            # num_sub_packets = int(packet[i : operator_len + i + 1])
        else:
            # length of sub packets
            operator_len = 15
            # len_sub_packets = int(packet[i : operator_len + i + 1])
        i += operator_len
        return version + p1(packet[i:])


def p2(packet, i=0):
    operator_functions = [
        sum,  # sum
        utils.list_product,  # product
        min,  # minimum
        max,  # maximum
        None,  # literal
        # 1 if first sub packet is greater than second sub packet else 0 (always have exactly two sub packets)
        lambda x: int(x[0] > x[1]),
        # 1 if first sub packet is less than second sub packet else 0 (always have exactly two sub packets)
        lambda x: int(x[0] < x[1]),
        # 1 if first sub packet is equal to the second sub packet else 0 (always have exactly two sub packets)
        lambda x: int(x[0] == x[1]),
    ]
    print(f"\ncall {i}\n{packet[i:]}")
    # while i < len(packet):

    i += 3  # skip over the version number
    id_type = int(packet[i : i + 3], 2)
    i += 3  # move pointer to after type id

    # literal - base case
    if id_type == 4:
        literal_str = ""
        while packet[i] == "1":
            literal_str += packet[i + 1 : i + 5]
            i += 5
        literal_str += packet[i + 1 : i + 5]
        i += 5
        literal = int(literal_str, 2)
        print("literal", literal)
        return literal, i

    # operator - recursive
    else:
        print("operator", id_type, "\n", packet[i:])
        # type length id
        type_len_id = packet[i]
        i += 1

        sub_packets = []

        # number of sub packets
        if type_len_id == "1":
            operator_len = 11
            num_sub_packets = int(packet[i : operator_len + i], 2)
            print(f"sub by cnt ({num_sub_packets})")
            i += operator_len
            before_i = i
            for _ in range(num_sub_packets):
                print("before", before_i)
                sub_packet_res, i = p2(packet, i)
                print("before", before_i, "returned", i, sub_packet_res)
                sub_packets.append(sub_packet_res)
                # if i >= len(packet) - 8:
                #     break

        # length of sub packets
        else:
            operator_len = 15
            len_sub_packets = int(packet[i : operator_len + i], 2)
            print(f"sub by len ({len_sub_packets})")
            i += operator_len
            len_sub_packets += i
            while i < len_sub_packets:
                sub_packet_res, i = p2(packet, i)
                sub_packets.append(sub_packet_res)

        print(f"={id_type}", sub_packets, "[", packet[i:], "]")
        return operator_functions[id_type](sub_packets), i


# _p1 = None  # p1(packet)
_p2, _ = p2(packet)

# print(f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}")

print(f"p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}")
