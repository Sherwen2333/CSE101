# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 12

# Part I
def extract_bits_3_9(num):
    mask = int('1111111111', 2)
    num &= mask
    num >>= 3
    return num


# Part II
def set_bits(num, bits_to_set):
    for izzz in bits_to_set:
        uzzz = 1 << izzz
        if (num >> izzz & 1 is 0):
            num += uzzz
    return num


# Part III
def decode_instruction(inst):
    izzzzzz = [0, 0, 0, 0]
    qwerty = int('11111111000000000000000000000000', 2)
    izzzzzz[0] = (inst & qwerty) >> 24
    inst = inst << 4
    inst = inst >> 4
    qwerty = int('111111110000000000000000', 2)
    izzzzzz[1] = (inst & qwerty) >> 16
    if (izzzzzz[0] < 4):
        inst = inst << 4
        inst = inst >> 4
        qwerty = int('1111111100000000 ', 2)
        izzzzzz[2] = (inst & qwerty) >> 8
        inst = inst << 4
        inst = inst >> 4
        qwerty = int('11111111', 2)
        izzzzzz[3] = (inst & qwerty)
        if izzzzzz[1] > 10 or izzzzzz[2] > 10 or izzzzzz[3] > 10:
            return (-1, -1, -1, -1)
        return tuple(izzzzzz)
    else:
        if izzzzzz[0] is not 4 or izzzzzz[1] > 10:
            return (-1, -1, -1, -1)
        return (izzzzzz[0], izzzzzz[1], inst & int('1111111111111111', 2))
