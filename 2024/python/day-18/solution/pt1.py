# Approach
#

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
    with open(file_path, 'r') as file:
        for line in file:
            line_num+= 1
            if line_num > limit:
                break
            col, row = line.rstrip().split(',')
            col = int(col)
            row = int(row)
            matrix[row][col] = '#'

    # for r in matrix:
    #     print(r)
    return matrix

def loc_to_key(loc: list[int]):
    return f"{loc[0]}_{loc[1]}"

def populate_solved_paths(path: list[str]):
    solved_paths: dict[str,int] = {}
    for i in range(len(path)):
        loc = path[i]
        key = loc_to_key(loc)
        solved_paths[key] = i

    return solved_paths


def find_min_path(route_matrix: list[list[str]], start: list[int], end: list[int]):
    starting_points = [
        {
            'loc': [start[0],start[1]],
            'score': 0
        }
    ]
    max_row = len(route_matrix) - 1
    max_col = len(route_matrix[0]) - 1

    solved_paths: dict[str, int] = {}

    shortest_path = 0

    while len(starting_points) > 0:
        start = starting_points.pop()
        # print('start', start)

        loc, score = start.values()
        new_score = score + 1

        for increment in DIRECTION_INCREMENTS:
            new_loc = [loc[0] + increment[0], loc[1] + increment[1]]
            new_loc_key = loc_to_key(new_loc)

            r,c = new_loc
            
            if r < 0 or r > max_row or c < 0 or c > max_col:
                continue

            char = route_matrix[r][c]
            if char == '#':
                continue
            
            # if it took longer to get to a solved point, just quit
            if new_loc_key in solved_paths:
                old_score = solved_paths[new_loc_key]
                if old_score <= new_score:
                    continue

            solved_paths[new_loc_key] = new_score

            if new_loc == end:
                shortest_path = new_score
            if char == '.':
                starting_points.append({
                    'loc': new_loc,
                    'score': new_score
                })

    return shortest_path

# seeded_matrix = seed_matrix('../input/sample.txt', 7, 12)
seeded_matrix = seed_matrix('../input/full.txt', 71, 1024)

min = find_min_path(seeded_matrix, [0,0], [len(seeded_matrix) - 1,len(seeded_matrix) -1])

print('min', min)


