# Approach
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
    start_location = {
        'r': 0,
        'c': 0,
        'dir' : DIRECTIONS['right']
    }
    end_location = {
        'r': 0,
        'c': 0
    }
    route_matrix: list[list[str]] = []
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            route_matrix.append(curr_line)

            if 'S' in curr_line:
                start_location['r'] = len(route_matrix) - 1
                start_location['c'] = curr_line.index('S')
                print('start loc', start_location)
            if 'E' in curr_line:
                end_location['r'] = len(route_matrix) - 1
                end_location['c'] = curr_line.index('E')
                print('end loc', end_location)

    return route_matrix, start_location, end_location

def loc_to_key(loc: dict[str,int]):
    return f"{loc['r']}-{loc['c']}"

def get_all_paths(route_matrix: list[list[str]], start_location: dict[str, int], end_location: dict[str,int]):
    paths_crossed: set[str] = set()
    paths_crossed.add(loc_to_key(start_location))
    loc_dir_score: dict[str, int] = {}
    successful_scores = []
    successful_paths = []

    # print(paths_crossed)
    checked_paths = 0

    starting_points = [
        {
            'reindeer': copy.deepcopy(start_location),
            'paths': copy.deepcopy(paths_crossed),
            'score': 0
        }
    ]

    while len(starting_points) > 0:
        checked_paths+= 1

        if (checked_paths % 10000) == 0:
            print('check num', checked_paths)
            print('still to check', len(starting_points))
        # if (checked_paths > 1000000):
            # break
        curr_point = starting_points.pop()
        reindeer, paths, score = curr_point.values()

        if score > 78428:
            continue
        # if score > 11048:
            # continue
        # if score > 7036:
        #     continue

        # print('checking r: ', reindeer['r'], ' c: ', reindeer['c'])

        forward_increment = DIRECTION_INCREMENTS[reindeer['dir']]
        left_increment = DIRECTION_INCREMENTS[(reindeer['dir'] - 1)%4]
        right_increment = DIRECTION_INCREMENTS[(reindeer['dir'] + 1)%4]

        fwd_loc = {
            'reindeer': {
                'r': reindeer['r'] + forward_increment[0],
                'c': reindeer['c'] + forward_increment[1],
                'dir': reindeer['dir']
            },
            'score': 1,
        }
        left_loc = {
            'reindeer': {
                'r': reindeer['r'] + left_increment[0],
                'c': reindeer['c'] + left_increment[1],
                'dir': (reindeer['dir'] - 1)%4
            },
            'score': 1001,
        }
        right_loc = {
            'reindeer': {
                'r': reindeer['r'] + right_increment[0],
                'c': reindeer['c'] + right_increment[1],
                'dir': (reindeer['dir'] + 1)%4
            },
            'score': 1001,
        }

        new_locs = [left_loc, right_loc, fwd_loc]

        for new_loc in new_locs:
            new_reindeer = new_loc['reindeer']
            new_loc_key = loc_to_key(new_reindeer)
            new_loc_dir_key = f"{new_loc_key}-{new_reindeer['dir']}"
            new_score = score+new_loc['score']

            spot = route_matrix[new_reindeer['r']][new_reindeer['c']]

            if new_loc_dir_key in loc_dir_score:
                if loc_dir_score[new_loc_dir_key] < new_score:
                    # print('optimize?')
                    continue
            loc_dir_score[new_loc_dir_key] = new_score

            # if new_loc_key in paths:
                # print('DOUBLED BACK')
                # continue
            
            if spot == '#':
                # print('FOUND WALL')
                continue

            if spot == 'E':
                print('********found end!********')
                paths.add(new_loc_key)
                score = new_score
                print(score)
                print(paths)
                successful_scores.append(score)
                successful_paths.append(paths)
                continue

            # print('spot', spot)
            new_paths = copy.deepcopy(paths)
            new_paths.add(new_loc_key)
            new_start = {
                'reindeer': copy.deepcopy(new_loc['reindeer']),
                'paths': new_paths,
                'score': new_score
            }

            # loc_dir_score[new_loc_dir_key] = new_score
            starting_points.append(new_start)
            
    return successful_scores, successful_paths


# route_matrix, start_location, end_location = read_file_two_d_array('../input/sample1.txt')
# route_matrix, start_location, end_location = read_file_two_d_array('../input/sample2.txt')
route_matrix, start_location, end_location = read_file_two_d_array('../input/full.txt')

paths, successful_paths = get_all_paths(route_matrix, start_location, end_location)

print(paths)

print(min(paths))

all_paths: set[str] = set()
for path in successful_paths:
    # print(path)
    all_paths = all_paths.union(path)

print(sorted(list(all_paths)))
print(len(all_paths))
