import re

def get_indices(pattern: str, target: str):
    
    indices: list[int] = list()

    for match in re.finditer(pattern, target):
        indices.append(match.start())

    return indices

def get_product(mul_string: str):
    nums_strs = re.findall(r"\d+", mul_string)
    nums_ints = list(map(int, nums_strs))

    return nums_ints[0] * nums_ints[1]

def get_muls_totals_from_string(stripped_str: str):
    tally =0

    muls = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)",stripped_str)

    print(muls)

    # print(muls)
    for str in muls:
        tally += get_product(str)

    return tally


def read_file(file_path):
    tally: int = 0
    is_doing = True

    with open(file_path, 'r') as file:
        for line in file:

            donts = get_indices(r"don't", line)

            # Find the dos & donts by index
            dos_and_donts = get_indices(r"do", line)

            left_idx=0
            # right_idx=0

            for i in range(len(dos_and_donts)):
                curr_do_or_dont = dos_and_donts[i]
                is_curr_do = curr_do_or_dont not in donts

                if is_doing and not is_curr_do:
                    # print('found a dont, total from left to here')
                    is_doing=False
                    tally+= get_muls_totals_from_string(line[left_idx:curr_do_or_dont])
                elif not is_doing and is_curr_do:
                    # print('found a do, make new left')
                    left_idx = curr_do_or_dont
                    is_doing=True
                
            # if ended with a do, add up rest of string
            if is_doing:
                tally+= get_muls_totals_from_string(line[curr_do_or_dont:])

    return tally

tally = read_file('../input/full.txt')

print(tally)

