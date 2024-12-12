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

def count_rock_blink(rock_blink: dict[str, str], count_by_stone_blinks: dict[str, int]):
    rock_val = rock_blink['r']
    num_blinks = rock_blink['blinks']

    key = f"{rock_val}-{num_blinks}"

    if key in count_by_stone_blinks:
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

# rock_str = read_file('../input/sample.txt')
rock_str = read_file('../input/full.txt')

rocks = create_rocks(rock_str)
num_stones = num_stones_by_blinks(rocks, 75)

print(num_stones)
