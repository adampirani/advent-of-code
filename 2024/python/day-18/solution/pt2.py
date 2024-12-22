DIRECTION_INCREMENTS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def seed_matrix(file_path: str, dimensions: int, limit: int):
    matrix: list[list[str]] = []
    for r in range(dimensions):
        row: list[str] = []
        for c in range(dimensions):
            row.append('.')
        matrix.append(row)
    
    line_num = 0
    future_bytes = []
    with open(file_path, 'r') as file:
        for line in file:
            line_num+= 1
            
            col, row = line.rstrip().split(',')
            col = int(col)
            row = int(row)
            if line_num > limit:
                future_bytes.append([row, col])
            else:
                matrix[row][col] = '#'

    return matrix, future_bytes

def loc_to_key(loc: list[int]):
    return f"{loc[0]}_{loc[1]}"

def populate_solved_paths(path: list[str]):
    solved_paths: dict[str,int] = {}
    for i in range(len(path)):
        loc = path[i]
        key = loc_to_key(loc)
        solved_paths[key] = i

    return solved_paths


def find_a_path(route_matrix: list[list[str]], start: list[int], end: list[int]):
    starting_points = [[start[0],start[1]]]
    paths_crossed: set[str] = {loc_to_key(start)}

    max_row = len(route_matrix) - 1
    max_col = len(route_matrix[0]) - 1

    solved_paths: dict[str, int] = {}

    shortest_path = 0

    while len(starting_points) > 0:
        loc = starting_points.pop()

        for increment in DIRECTION_INCREMENTS:
            new_loc = [loc[0] + increment[0], loc[1] + increment[1]]
            new_loc_key = loc_to_key(new_loc)

            if new_loc_key in paths_crossed:
                continue

            r,c = new_loc
            
            if r < 0 or r > max_row or c < 0 or c > max_col:
                continue

            char = route_matrix[r][c]
            if char == '#':
                continue
            paths_crossed.add(new_loc_key)

            if new_loc == end:
                return True
            if char == '.':
                starting_points.append(new_loc)

    return False

# seeded_matrix, future_bytes = seed_matrix('../input/sample.txt', 7, 12)
seeded_matrix, future_bytes = seed_matrix('../input/full.txt', 71, 1024)

for byte in future_bytes:
    seeded_matrix[byte[0]][byte[1]] = '#'

    if not find_a_path(seeded_matrix, [0,0], [len(seeded_matrix) - 1, len(seeded_matrix) -1]):
        print('failed on byte', f"{byte[1]},{byte[0]}")
        break




