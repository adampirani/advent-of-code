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

def process_instructions(warehouse: list[list[str]], robot_location: dict[str, int], instructions: list[str]):

    for instruction_set in instructions:
        for instruction in instruction_set:
            print('processing: ', instruction)
            increment = DIRECTION_INCREMENTS[DIRECTIONS[instruction]]

            next_row = robot_location['row'] + increment[0]
            print('new row', next_row)
            next_col = robot_location['col'] + increment[1]
            print('new col', next_col)

            while True:
                next_item = warehouse[next_row][next_col]
                # print('next_item', next_item)
                if next_item == '#':
                    break
                if next_item == '.':
                    increment = 1 if instruction in ['<', '^'] else -1
                    if instruction in ['<', '>']:
                        warehouse[robot_location['row']][robot_location['col']] = '.'
                        for i in range(next_col, robot_location['col'], increment):
                            warehouse[next_row][i] = warehouse[next_row][i + increment]
                            robot_location = {
                                'row': next_row,
                                'col': i
                            }
                        print('updateing row: ', robot_location['row'])
                        print('updateing col: ', robot_location['col'])
                        warehouse[robot_location['row']][robot_location['col']] = '@'
                    else:
                        # if one space away just move
                        if next_row == robot_location['row'] - increment:
                            print('one space away')
                            warehouse[robot_location['row']][robot_location['col']] = '.'
                            robot_location = {
                                'row': next_row,
                                'col': next_col
                            }
                            warehouse[robot_location['row']][robot_location['col']] = '@'
                        else:
                            print('deal w/ boxes')
                            # from robot to end point
                            # find a box one away
                            # for all the boxes in that row, up to (but not including) the end row, get all boxes
                            # touched by boxes in that row

                            robot_r = robot_location['row']
                            robot_c = robot_location['col']

                            next_box_part = warehouse[robot_r - increment][robot_c]
                            rows_of_boxes_to_move = []

                            current_row = robot_r - increment
                            if next_box_part == '[':
                                rows_of_boxes_to_move.append([{'r': current_row, 'c': robot_c}])
                            else: 
                                rows_of_boxes_to_move.append([{'r': current_row, 'c': robot_c -1}])

                            
                            #get all the boxes
                            is_box_blocked = False
                            print('current row', current_row)
                            print('nnext row', next_row)
                            while current_row  != next_row - increment:
                                print('current row', current_row)
                                print('nnext row', next_row)
                                current_row -= increment
                                warehouse_row = warehouse[current_row]
                                print('warehouse_row to process', warehouse_row)
                                # if anything above a box in this row is a wall, stop
                                row_of_boxes_to_check = rows_of_boxes_to_move[-1]
                                print('row_of_boxes_to_check', row_of_boxes_to_check)
                                boxes_to_add = set()
                                new_row_boxes = []
                                for box in row_of_boxes_to_check:
                                    next_left = warehouse_row[box['c']]
                                    next_right = warehouse_row[box['c']-increment]
                                    if next_left == '#' or next_right == '#':
                                        is_box_blocked = True
                                        print('BOX BLOCKED')
                                        break
                                    if next_left == '[':
                                        boxes_to_add.add(box['c'])
                                    if next_right == '[':
                                        boxes_to_add.add(box['c']+1)
                                    if next_left == ']':
                                        boxes_to_add.add(box['c']-1)
                                    if next_right == ']':
                                        boxes_to_add.add(box['c'])

                                print('boxes_to_add', boxes_to_add)

                                if is_box_blocked:
                                    break

                                for box in boxes_to_add:
                                    new_row_boxes.append({'r': current_row, 'c': box})

                                rows_of_boxes_to_move.append(new_row_boxes)

                            if is_box_blocked:
                                break
                                
                            #move all the boxes
                            print('rows of boxes to move: ', rows_of_boxes_to_move)
                            rows_of_boxes_to_move.pop()
                            while len(rows_of_boxes_to_move) > 0:
                                row_to_process = rows_of_boxes_to_move.pop()

                                # print('move boxes in this row', row_to_process)

                                for box in row_to_process:
                                    box_r = box['r']
                                    box_c = box['c']
                                    warehouse[box_r - increment][box_c] = '['
                                    warehouse[box_r - increment][box_c + 1] = ']'
                                    warehouse[box_r][box_c] = '.' 
                                    warehouse[box_r][box_c+1] = '.' 
                                
                                # for i in range(robot_location['row'] - increment, next_row, -increment):
                                #     warehouse[i][next_col] = warehouse[i + increment][next_col]
                                #     robot_location = {
                                #         'row': i,
                                #         'col': next_col
                                #     }
                            warehouse[robot_r][robot_c] = '.'
                            warehouse[robot_r - increment][robot_c] = '@'
                            robot_location['row'] = robot_r - increment
                            robot_location['col'] = robot_c
                    break

                next_row += increment[0]
                next_col += increment[1]
            
            for ware_house_line in warehouse:
                print(''.join(ware_house_line))

    return warehouse

def calc_box_coords(warehouse: list[list[str]]):
    count = 0
    for r in range(len(warehouse)):
        row = warehouse[r]
        for c in range(len(row)):
            if warehouse[r][c] == '[':
                count+= 100*r + c

    return count


# warehouse, robot_location, instructions = read_file_two_d_array('../input/mini2.txt')
# warehouse, robot_location, instructions = read_file_two_d_array('../input/sample.txt')
# warehouse, robot_location, instructions = read_file_two_d_array('../input/full.txt')

warehouse = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
['#', '#', '[', ']', '.', '.', '[', ']', '.', '.', '.', '.', '[', ']', '.', '.', '[', ']', '#', '#'],
['#', '#', '[', ']', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '.', '.', '#', '#'],
['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '[', ']', '[', ']', '#', '#'],
['#', '#', '.', '.', '.', '.', '.', '.', '.', '@', '.', '[', ']', '.', '[', ']', '.', '.', '#', '#'],
['#', '#', '.', '.', '#', '#', '[', ']', '.', '.', '[', ']', '.', '.', '.', '.', '.', '.', '#', '#'],
['#', '#', '.', '.', '.', '[', ']', '.', '.', '.', '[', ']', '.', '.', '[', ']', '.', '.', '#', '#'],
['#', '#', '.', '.', '.', '.', '.', '[', ']', '.', '.', '[', ']', '.', '[', ']', '[', ']', '#', '#'],
['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '[', ']', '.', '.', '.', '.', '.', '.', '#', '#'],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

robot_location = {
    'row': 4,
    'col': 9
}

print('robot loc: ', robot_location)

for ware_house_line in warehouse:
    print(''.join(ware_house_line))

updated_warehouse = process_instructions(warehouse, robot_location, '>v')
# updated_warehouse = process_instructions(warehouse, robot_location, instructions)

for ware_house_line in updated_warehouse:
    print(''.join(ware_house_line))

total_box_coords = calc_box_coords(updated_warehouse)

print(total_box_coords)

