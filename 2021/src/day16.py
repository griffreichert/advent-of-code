import utils

lines = utils.read_list(__file__, as_str=True)

# read in each char as an int (convert hex to decimal, then interpret it as a 4 bit 0 padded binary string)
packet = "".join(f"{int(char, base=16):04b}" for char in lines[0])


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
        else:
            operator_len = 15
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

    id_type = int(packet[i + 3 : i + 6], 2)
    i += 6  # move pointer to after type id

    # literal - base case
    if id_type == 4:
        literal_binary = ""
        # while the first bit is a 1, read the next 4 bits as part of the literal
        while packet[i] == "1":
            literal_binary += packet[i + 1 : i + 5]
            i += 5
        # literals always end with a 0 bit then 4 bits
        literal_binary += packet[i + 1 : i + 5]
        i += 5
        # convert the binary string into decimal, return the new position after the literal
        return int(literal_binary, 2), i

    # operator - recursive
    else:
        # type length id
        type_len_id = packet[i]
        i += 1

        sub_packets = []

        # number of sub packets
        if type_len_id == "1":
            operator_len = 11
            # parse out the number of sub packets
            num_sub_packets = int(packet[i : operator_len + i], 2)
            i += operator_len
            # iterate over the sub packets
            for _ in range(num_sub_packets):
                sub_packet_res, i = p2(packet, i)
                sub_packets.append(sub_packet_res)

        # length of sub packets
        else:
            operator_len = 15
            len_sub_packets = int(packet[i : operator_len + i], 2)
            i += operator_len
            # move the range to be i:i+len
            len_sub_packets += i
            while i < len_sub_packets:
                sub_packet_res, i = p2(packet, i)
                sub_packets.append(sub_packet_res)

        return operator_functions[id_type](sub_packets), i


_p1 = p1(packet)
_p2, _ = p2(packet)


print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
