# Approach

# Convert file into two-d array of strings
# move through array until an 'x' is found
# search all 8 directions for xmas, add 1 for each
#

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

def process_matrix(route_matrix: list[list[str]], guard_location: dict[str, int]):
    paths_crossed: set[str] = set()
    paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")

    print(paths_crossed)

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
            print('change direction', guard_location['direction'])
        else:
            guard_location['row'] = next_loc['row']
            guard_location['col'] = next_loc['col']
            paths_crossed.add(f"{guard_location['row']}-{guard_location['col']}")

    return len(paths_crossed)


route_matrix, guard_location = read_file_two_d_array('../input/full.txt')

print(route_matrix, guard_location)

count = process_matrix(route_matrix, guard_location)

print(count)

