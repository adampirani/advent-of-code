# Approach


DIRECTIONS = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}

DIRECTION_INCREMENTS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def read_file_two_d_array(file_path):
    robot_location = {
        'row': 0,
        'col': 0,
    }
    warehouse: list[list[str]] = []
    robot_found = False
    processing_warehouse = True
    instructions: list[str] = []
    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                processing_warehouse = False
                continue

            if processing_warehouse:
                curr_line = list(line.rstrip())
                warehouse.append(curr_line)

                if not robot_found and '@' in curr_line:
                    robot_found = True
                    robot_location['row'] = len(warehouse) - 1
                    robot_location['col'] = curr_line.index('@')
            else:
                instructions.append(line.rstrip())

    return warehouse, robot_location, instructions

def process_instructions(warehouse: list[list[str]], robot_location: dict[str, int], instructions: list[str]):
    for instruction_set in instructions:
        for instruction in instruction_set:
            increment = DIRECTION_INCREMENTS[DIRECTIONS[instruction]]

            next_row = robot_location['row'] + increment[0]
            next_col = robot_location['col'] + increment[1]

            while True:
                next_item = warehouse[next_row][next_col]
                # print('next_item', next_item)
                if next_item == '#':
                    break
                if next_item == '.':
                    increment = 1 if instruction in ['<', '^'] else -1
                    warehouse[robot_location['row']][robot_location['col']] = '.'
                    if instruction in ['<', '>']:
                        for i in range(next_col, robot_location['col'], increment):
                            warehouse[next_row][i] = warehouse[next_row][i + increment]
                            robot_location = {
                                'row': next_row,
                                'col': i
                            }
                        warehouse[robot_location['row']][robot_location['col']] = '@'
                    else:
                        for i in range(next_row, robot_location['row'], increment):
                            warehouse[i][next_col] = warehouse[i + increment][next_col]
                            robot_location = {
                                'row': i,
                                'col': next_col
                            }
                        warehouse[robot_location['row']][robot_location['col']] = '@'

                    break

                next_row += increment[0]
                next_col += increment[1]

    return warehouse

def calc_box_coords(warehouse: list[list[str]]):
    count = 0
    for r in range(len(warehouse)):
        row = warehouse[r]
        for c in range(len(row)):
            if warehouse[r][c] == 'O':
                count+= 100*r + c

    return count


# warehouse, robot_location, instructions = read_file_two_d_array('../input/mini.txt')
# warehouse, robot_location, instructions = read_file_two_d_array('../input/sample.txt')
warehouse, robot_location, instructions = read_file_two_d_array('../input/full.txt')

# for ware_house_line in warehouse:
#     print(ware_house_line)

updated_warehouse = process_instructions(warehouse, robot_location, instructions)

# for ware_house_line in updated_warehouse:
#     print(ware_house_line)

total_box_coords = calc_box_coords(updated_warehouse)

print(total_box_coords)

