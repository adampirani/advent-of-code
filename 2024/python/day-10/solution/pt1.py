def read_file_two_d_array(file_path):

    t_map: list[list[int]] = []
    start_locations: list[dict[str,str]] = list()
    r = 0
    with open(file_path, 'r') as file:
        for line in file:
            trail_row: list[int] = []
            curr_line = list(line.rstrip())

            for c in range(len(curr_line)):
                char = curr_line[c]
                trail_row.append(char)
                if char == '0':
                    coords = {'r': r, 'c': c}
                    start_locations.append(coords)

            t_map.append(trail_row)
            r+= 1
    return t_map, start_locations

FOUR_DIRECTIONS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def count_trailheads(t_map: list[list[str]], loc: dict[str,str]):
    found_nines: set[str] = set()

    coords_to_track = [loc]
    max_r = len(t_map)
    max_c = len(t_map[0])

    while len(coords_to_track) > 0:
        # print('coords_to_track', coords_to_track)

        current_coord = coords_to_track.pop()
        row, col = current_coord['r'], current_coord['c']
        coord_val = int(t_map[row][col])

        # print('row', row)
        # print('col', col)
        # print('cood_val', coord_val)

        if coord_val == 9:
            found_nines.add(f"{row}-{col}")
            continue

        for dir in FOUR_DIRECTIONS:
            dir_r, dir_c = dir
            new_r = row + dir_r
            new_c = col + dir_c
            
            if new_r in range(0, max_r) and new_c in range(0, max_c):
                new_coord_val = t_map[new_r][new_c]
                if new_coord_val != '.':

                    if int(new_coord_val) == coord_val+1:
                        coords_to_track.append({
                            'r': new_r,
                            'c': new_c
                        })

    return len(found_nines)

def get_trailhead_sums(t_map: list[list[str]], start_locations: list[dict[str,str]]):
    sum = 0

    for loc in start_locations:
        sum+= count_trailheads(t_map, loc)

    return sum

# t_map, start_locations = read_file_two_d_array('../input/sample.txt')
t_map, start_locations = read_file_two_d_array('../input/full.txt')

# print(t_map)
# print(start_locations)

sum = get_trailhead_sums(t_map, start_locations)

print(sum)
