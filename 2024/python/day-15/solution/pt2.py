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
                curr_line = []
                for char in line.rstrip():
                    if char == '@':
                        curr_line.append('@')
                        robot_location['row'] = len(warehouse)
                        robot_location['col'] = len(curr_line) - 1
                        curr_line.append('.')
                    elif char == 'O':
                        curr_line.append('[')
                        curr_line.append(']')
                    else:
                        curr_line.append(char)
                        curr_line.append(char)
                warehouse.append(curr_line)
            else:
                instructions.append(line.rstrip())

    return warehouse, robot_location, instructions

def get_boxes(rows_of_boxes: list[list[dict[str, int]]], step: int, warehouse: list[list[str]]):
    # print('get boxes step', step)
    all_boxes = rows_of_boxes
    next_row_box_cols = set()
    previous_row = rows_of_boxes[-1]
    for box_col in previous_row:
        # if box is blocked return False
        box_r = box_col['r']
        box_c = box_col['c']
        next_left = warehouse[box_r + step][box_c]
        next_right = warehouse[box_r + step][box_c+1]
        if next_left == '#' or next_right == '#':
            return True, rows_of_boxes
        if next_left == '[':
            next_row_box_cols.add(box_c)
        if next_left == ']':
            next_row_box_cols.add(box_c-1)
        if next_right == '[':
            next_row_box_cols.add(box_c+1)
        if next_right == ']':
            next_row_box_cols.add(box_c)
    if len(next_row_box_cols) == 0:
        return False, all_boxes
    
    next_row = []
    for box_col in next_row_box_cols:
        next_row.append({
            'r': box_r + step,
            'c': box_col
        })
    all_boxes.append(next_row)

    return get_boxes(all_boxes, step, warehouse)

def move_boxes(rows_of_boxes: list[list[dict[str, int]]], step: int, warehouse: list[list[str]]):

    while len(rows_of_boxes) > 0:
        row_to_move = rows_of_boxes.pop()
        for box in row_to_move:
            box_r = box['r']
            box_c = box['c']
            warehouse[box_r + step][box_c] = '['
            warehouse[box_r + step][box_c+1] = ']'
            warehouse[box_r][box_c] = '.'
            warehouse[box_r][box_c+1] = '.'

    return warehouse


def process_instructions(warehouse: list[list[str]], robot_location: dict[str, int], instructions: list[str]):

    for instruction_set in instructions:
        # print('instruction_set', instruction_set)
        for instruction in instruction_set:
            # print('processing: ', instruction)
            increment = DIRECTION_INCREMENTS[DIRECTIONS[instruction]]

            next_row = robot_location['row'] + increment[0]
            # print('new row', next_row)
            next_col = robot_location['col'] + increment[1]
            # print('new col', next_col)

            step = -1 if instruction in ['<', '^'] else 1

            next_item = warehouse[next_row][next_col]
            # print('next_item', next_item)
            if next_item == '#':
                # print('blocked no change')
                continue
            if next_item == '.':
                warehouse[robot_location['row']][robot_location['col']] = '.'
                robot_location = {
                    'row': next_row,
                    'col': next_col
                }
                warehouse[robot_location['row']][robot_location['col']] = '@'
            else:
                # print('deal w/ boxes')
                if instruction in ['<', '>']:
                    # print('l/r boxes, keep going until wall or space')
                    while next_item != '#' and next_item != ".":
                        next_col += step
                        next_item = warehouse[next_row][next_col]
                    if next_item == '.':
                        for i in range(next_col, robot_location['col'], -step):
                            warehouse[next_row][i] = warehouse[next_row][i - step]
                        warehouse[robot_location['row']][robot_location['col']] = '.'
                        robot_location = {
                            'row': next_row,
                            'col': robot_location['col'] + step
                        }
                        warehouse[robot_location['row']][robot_location['col']] = '@'
                else:
                    # print('up/down, deal with complex')
                    first_box = {
                        'r': next_row,
                        'c': next_col
                    }
                    if next_item == ']':
                        first_box['c']-= 1

                    rows_of_boxes = [[first_box]]

                    is_blocked, all_boxes = get_boxes(rows_of_boxes, step, warehouse)

                    # print('is blocked: ', is_blocked)

                    if not is_blocked:
                        # print('move boxes', all_boxes)
                        warehouse = move_boxes(all_boxes, step, warehouse)
                        warehouse[robot_location['row']][robot_location['col']] = '.'
                        robot_location = {
                            'row': robot_location['row'] + step,
                            'col': robot_location['col']
                        }
                        warehouse[robot_location['row']][robot_location['col']] = '@'

            # for ware_house_line in warehouse:
            #     print(''.join(ware_house_line))

    return warehouse

def calc_box_coords(warehouse: list[list[str]]):
    count = 0
    for r in range(len(warehouse)):
        row = warehouse[r]
        for c in range(len(row)):
            if warehouse[r][c] == '[':
                count+= 100*r + c

    return count


# warehouse, robot_location, instructions = read_file_two_d_array('../input/mini.txt')
# warehouse, robot_location, instructions = read_file_two_d_array('../input/sample.txt')
warehouse, robot_location, instructions = read_file_two_d_array('../input/full.txt')

# warehouse = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# ['#', '#', '[', ']', '.', '.', '[', ']', '.', '.', '.', '.', '[', ']', '.', '.', '[', ']', '#', '#'],
# ['#', '#', '[', ']', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '.', '.', '#', '#'],
# ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '[', ']', '[', ']', '#', '#'],
# ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '.', '[', ']', '.', '.', '#', '#'],
# ['#', '#', '.', '.', '#', '#', '[', ']', '.', '@', '[', ']', '[', ']', '.', '.', '.', '.', '#', '#'],
# ['#', '#', '.', '.', '.', '[', ']', '.', '.', '.', '[', ']', '.', '.', '[', ']', '.', '.', '#', '#'],
# ['#', '#', '.', '.', '.', '.', '.', '[', ']', '.', '.', '[', ']', '.', '[', ']', '[', ']', '#', '#'],
# ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '.', '.', '.', '.', '.', '.', '#', '#'],
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# robot_location = {
#     'row': 5,
#     'col': 9
# }

print('robot loc: ', robot_location)

for ware_house_line in warehouse:
    print(''.join(ware_house_line))

# updated_warehouse = process_instructions(warehouse, robot_location, '>>>>>>')
updated_warehouse = process_instructions(warehouse, robot_location, instructions)

for ware_house_line in updated_warehouse:
    print(''.join(ware_house_line))

total_box_coords = calc_box_coords(updated_warehouse)

print(total_box_coords)

