# Approach

# Convert file into two-d array of strings
# move through array until an 'x' is found
# search all 8 directions for xmas, add 1 for each
#

import copy

DIRECTIONS = {
    'up': 0,
    'right': 1,
    'down': 2,
    'left': 3
}

DIRECTION_INCREMENTS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def read_file_two_d_array(file_path):
    guard_location = {
        'row': 0,
        'col': 0,
        'direction' : DIRECTIONS['up']

    }
    route_matrix: list[list[str]] = []
    guard_found = False
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            route_matrix.append(curr_line)

            if not guard_found and '^' in curr_line:
                guard_found = True
                guard_location['row'] = len(route_matrix) - 1
                guard_location['col'] = curr_line.index('^')
                print('guard_loc', guard_location)

    return route_matrix, guard_location

def process_matrix(route_matrix: list[list[str]], og_guard_location: dict[str, int]):
    guard_location = copy.deepcopy(og_guard_location)
    paths_crossed: set[str] = set()
    # paths_crossed_w_dir: set[str] = set()
    paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")
    # paths_crossed_w_dir.add(f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}")

    # print(paths_crossed)

    num_cols = len(route_matrix)
    num_rows = len(route_matrix[0])

    while True:
        if guard_location['row'] == 0:
            break
        if guard_location['row'] == num_rows -1:
            break
        if guard_location['col'] == 0:
            break
        if guard_location['col'] == num_cols -1:
            break

        increment = DIRECTION_INCREMENTS[guard_location['direction']]

        next_loc = {
            'row': guard_location['row'] + increment[0],
            'col': guard_location['col'] + increment[1]
        }

        if route_matrix[next_loc['row']][next_loc['col']] == '#':
            guard_location['direction'] += 1
            guard_location['direction'] =  guard_location['direction']%len(DIRECTIONS)
            # print('change direction', guard_location['direction'])
        else:
            guard_location['row'] = next_loc['row']
            guard_location['col'] = next_loc['col']
            paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")
            # paths_crossed_w_dir.add(f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}")

    return len(paths_crossed)


# route_matrix, guard_location = read_file_two_d_array('../input/sample.txt')
route_matrix, guard_location = read_file_two_d_array('../input/full.txt')

# print(route_matrix, guard_location)

print('guard location before', guard_location)
count = process_matrix(route_matrix, guard_location)
print('guard location after', guard_location)

print(count)
# print(paths_crossed_w_dir)

def is_loop(fake_matrix: list[list[str]], og_guard_location: dict[str, int]):
    guard_location = copy.deepcopy(og_guard_location)

    paths_crossed_w_dir: set[str] =  set()

    # print('is loop')
    # print('fake_matrix', fake_matrix)
    # print('guard_location', guard_location)
    # print('paths_crossed_w_dir', paths_crossed_w_dir)

    num_cols = len(fake_matrix)
    num_rows = len(fake_matrix[0])

    running_around_count = 0

    while True:
        running_around_count+=1

        if (running_around_count > 10000):
            print('********************trapped ?')
            return True
        if guard_location['row'] == 0:
            # print('NO LOOP')
            return False
        if guard_location['row'] == num_rows -1:
            # print('NO LOOP')
            return False
        if guard_location['col'] == 0:
            # print('NO LOOP')
            return False
        if guard_location['col'] == num_cols -1:
            # print('NO LOOP')
            return False
        
        loc_w_dir = f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}"
        if loc_w_dir in paths_crossed_w_dir:
            # print('FOUND LOOP!')
            return True
        paths_crossed_w_dir.add(loc_w_dir)

        increment = DIRECTION_INCREMENTS[guard_location['direction']]

        # next_loc = {
        #     'row': guard_location['row'] + increment[0],
        #     'col': guard_location['col'] + increment[1]
        # }
        next_r = guard_location['row'] + increment[0]
        next_c =  guard_location['col'] + increment[1]

        if fake_matrix[next_r][next_c] == '#':
            guard_location['direction'] += 1
            guard_location['direction'] =  guard_location['direction']%len(DIRECTIONS)
            # paths_crossed_w_dir.add(f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}")
            # print('change direction', guard_location['direction'])
        else:
            guard_location['row'] = next_r
            guard_location['col'] = next_c
            # paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")
            # paths_crossed_w_dir.add(f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}")

    return False

def count_loopers(route_matrix: list[list[str]], og_guard_location: dict[str, int]):
    guard_location = copy.deepcopy(og_guard_location)
    num_cols = len(route_matrix)
    num_rows = len(route_matrix[0])

    # print(route_matrix)

    blocked_paths = set()
    
    counter = 0

    while True:
        counter+= 1

        # print('guard_location', guard_location)
        # if counter > 3:
            # print('BAILEDING')
            # break

        if guard_location['row'] == 0:
            break
        if guard_location['row'] == num_rows -1:
            break
        if guard_location['col'] == 0:
            break
        if guard_location['col'] == num_cols -1:
            break

        increment = DIRECTION_INCREMENTS[guard_location['direction']]

        # next_loc = {
        #     'row': guard_location['row'] + increment[0],
        #     'col': guard_location['col'] + increment[1]
        # }
        next_r = guard_location['row'] + increment[0]
        next_c =  guard_location['col'] + increment[1]

        if route_matrix[next_r][next_c] == '#':
            guard_location['direction'] += 1
            guard_location['direction'] =  guard_location['direction']%len(DIRECTIONS)
            # print('change direction', guard_location['direction'])
        else:
            # find if adding a guard would make a loop
            potential_blocked_path = f"{next_r}-{next_c}"
            
            if potential_blocked_path not in blocked_paths:
                fake_matrix = copy.deepcopy(route_matrix)
                fake_matrix[next_r][next_c] = '#'
                
                if is_loop(fake_matrix, og_guard_location):
                    print('change at ', next_r, next_c)
                    # print('fake_matrix\n', fake_matrix)
                    # print('route_matrix\n', route_matrix)
                    blocked_paths.add(potential_blocked_path)

            guard_location['row'] = next_r
            guard_location['col'] = next_c
            # paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")
            # paths_crossed_w_dir.add(f"{guard_location['row']}-{guard_location['col']}-{guard_location['direction']}")

    return len(blocked_paths)

num_loopers = count_loopers(route_matrix, guard_location)

print('num loopers', num_loopers)

