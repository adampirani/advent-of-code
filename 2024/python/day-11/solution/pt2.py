# Approach


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.rstrip()

def create_rocks(rock_str: str):
    return list(map(int, rock_str.split(' ')))

def process_blink(rock: int):
    new_list = []
    if rock == 0:
        new_list.append(1)
    elif len(str(rock)) %2 == 0:
        rock_str = str(rock)
        mid_char = len(rock_str) // 2
        l_rock = int(rock_str[:mid_char])
        r_rock = int(rock_str[mid_char:])
        new_list.append(l_rock)
        new_list.append(r_rock)
    else:
        new_list.append(rock*2024)
    return new_list

# print('process_blink([0])', process_blink([0]))
# print('process_blink([1])', process_blink([1]))
# print('process_blink([10])', process_blink([10]))
# print('process_blink([1001])', process_blink([1001]))
# print('process_blink([99])', process_blink([99]))
# print('process_blink([999])', process_blink([999]))
# print('process_blink([999])', process_blink([999]))
# print('process_blink([1117,0,8,21078,2389032,142881,93,385])', process_blink([1117,0,8,21078,2389032,142881,93,385]))

global num_found_in_dict
num_found_in_dict = [0]

def count_rock_blink(rock_blink: dict[str, str], count_by_stone_blinks: dict[str, int]):
    rock_val = rock_blink['r']
    num_blinks = rock_blink['blinks']

    key = f"{rock_val}-{num_blinks}"

    if key in count_by_stone_blinks:
        num_found_in_dict[0] +=1
        return count_by_stone_blinks[key]
    
    if num_blinks == 0:
        return 1
    
    new_stones = process_blink(rock_val)

    sum = 0
    for stone in new_stones:
        new_rock_blink = {
            'r': stone,
            'blinks': num_blinks - 1
        }
        sum+= count_rock_blink(new_rock_blink, count_by_stone_blinks)
    
    count_by_stone_blinks[key] = sum

    return sum
    



def num_stones_by_blinks(rocks: list[int], num_blinks: int):
    count_by_stone_blinks = {}
    ttl_count = 0
    rock_blinks_to_process = []

    for rock in rocks:
        rock_blinks_to_process.append({'r': rock, 'blinks': num_blinks})

    while len(rock_blinks_to_process) > 0:
        rock_blink = rock_blinks_to_process.pop()
        ttl_count += count_rock_blink(rock_blink, count_by_stone_blinks)

    print('count by blinks dict len: ', len(count_by_stone_blinks))
    
    return ttl_count

#     l = 0
#     r = len(blocks) - 1
#     while l < r:
#         while blocks[l] != '.':
#             l+= 1
#         while blocks[r] == '.':
#             r-= 1

#         blocks[l] = blocks[r]
#         blocks[r] = '.'
#         l+=1
#         r-=1

# def calc_checksum(blocks: list[int|str]):
#     total = 0

#     for i in range(len(blocks)):
#         if blocks[i] == '.':
#             return total
#         total+= blocks[i] * i

#     return total


# rock_str = read_file('../input/sample.txt')
rock_str = read_file('../input/full.txt')

rocks = create_rocks(rock_str)
print('initial rocks: ', rocks)

num_stones = num_stones_by_blinks(rocks, 75)

# processed_rocks = blink_rocks(rocks, 6)
print(num_stones)

print('num_found_in_dict', num_found_in_dict)
