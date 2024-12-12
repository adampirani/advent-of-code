# Approach


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.rstrip()

def create_rocks(rock_str: str):
    return list(map(int, rock_str.split(' ')))

def process_blink(rocks: list[int]):
    new_list = []
    for rock in rocks:
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

MAX_LEN = 3

def blink_rocks(rocks: list[int], num_blinks: int):
    changing_rocks = rocks
    
    for i in range(num_blinks):
        print('blink num', i)
        changing_rocks = process_blink(changing_rocks)

    return changing_rocks



# rock_str = read_file('../input/sample.txt')
rock_str = read_file('../input/full.txt')

rocks = create_rocks(rock_str)
print('rocks: ', rocks)

# processed_rocks = blink_rocks(rocks, 6)
# print(processed_rocks)
processed_rocks = blink_rocks(rocks, 25)

print(len(processed_rocks))
