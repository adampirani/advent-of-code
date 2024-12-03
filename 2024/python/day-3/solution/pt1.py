import re

def get_product(mul_string: str):
    nums_strs = re.findall(r"\d+", mul_string)
    nums_ints = list(map(int, nums_strs))

    return nums_ints[0] * nums_ints[1]


def read_file(file_path):
    tally: int = 0

    with open(file_path, 'r') as file:
        for line in file:
            muls = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)",line)
            for str in muls:
                tally += get_product(str)
    return tally

tally = read_file('../input/full.txt')

print(tally)

