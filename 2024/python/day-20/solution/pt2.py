# Approach
#

DIRECTION_INCREMENTS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def read_file_two_d_array(file_path):
    start_location = [0,0]
    end_location = [0,0]
    route_matrix: list[list[str]] = []
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            route_matrix.append(curr_line)

            if 'S' in curr_line:
                start_location[0] = len(route_matrix) - 1
                start_location[1] = curr_line.index('S')
                print('start loc', start_location)
            if 'E' in curr_line:
                end_location[0] = len(route_matrix) - 1
                end_location[1] = curr_line.index('E')
                print('end loc', end_location)

    return route_matrix, start_location, end_location

def loc_to_key(loc: list[int]):
    return f"{loc[0]}_{loc[1]}"

def get_path_seconds(track: list[list[str]], start: list[int], end: list[int]):

    curr_point = {
        'loc': [start[0],start[1]],
        'score': 0
    }

    visited_points: dict[str, int] = {loc_to_key(curr_point['loc']): 0}

    # max_row = len(route_matrix) - 1
    # max_col = len(route_matrix[0]) - 1

    while curr_point['loc'] != end:
        loc, score = curr_point.values()
        new_score = score + 1

        for increment in DIRECTION_INCREMENTS:
            new_loc = [loc[0] + increment[0], loc[1] + increment[1]]
            new_loc_key = loc_to_key(new_loc)

            r,c = new_loc            
            # if r < 0 or r > max_row or c < 0 or c > max_col:
            #     continue

            char = track[r][c]
            if char == '#':
                continue

            if new_loc_key in visited_points:
                continue

            visited_points[new_loc_key] = new_score

            curr_point['loc'] = new_loc
            curr_point['score'] = new_score

    return visited_points

def get_cheats_by_times(path_seconds: dict[str, int], min_time: int):
    cheats_by_times: dict[int, list[str]] = {}

    loc_keys = list(path_seconds.keys())
    num_keys = len(loc_keys)

    for i in range(num_keys - min_time): 
        loc_key = loc_keys[i]
        loc = list(map(int, loc_key.split('_')))

        for j in range(i + min_time, num_keys):
            new_loc_key = loc_keys[j]            
            new_loc = list(map(int, new_loc_key.split('_')))
            time_taken = abs(new_loc[0] - loc[0]) + abs(new_loc[1] - loc[1])

            if time_taken > 20:
                continue

            cheat_val = path_seconds[new_loc_key] - path_seconds[loc_key] - time_taken
            # print('cheat val: ', cheat_val)

            if cheat_val < min_time:
                continue

            cheat_key = f"{loc_key}~{new_loc_key}"

            if cheat_val in cheats_by_times:
                cheats_by_times[cheat_val].append(cheat_key)
            else:
                cheats_by_times[cheat_val] = [cheat_key]
    
    return cheats_by_times

def num_cheats(cheats_by_time: dict[int,list[str]]):
    count = 0

    for key in cheats_by_time.keys():
        count+= len(cheats_by_time[key])
        # print(f"there are {len(cheats_by_time[key])} cheats that save {key} seconds")
    return count

# race_track, start, end = read_file_two_d_array('../input/sample.txt')
race_track, start, end = read_file_two_d_array('../input/full.txt')

path_seconds = get_path_seconds(race_track, start, end)
# print('path seconds', path_seconds)

# cheats_by_time = get_cheats_by_times(path_seconds, 50)
cheats_by_time = get_cheats_by_times(path_seconds, 100)
count = num_cheats(cheats_by_time)

print('count: ', count)


