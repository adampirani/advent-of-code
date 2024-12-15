# Approach

from functools import reduce

# WIDTH = 11
WIDTH = 101
# HEIGHT = 7
HEIGHT = 103
SECONDS = 100

INVALID_COL = WIDTH//2
INVALID_ROW = HEIGHT//2

# print('INVALID col', INVALID_COL)
# print('INVALID row', INVALID_ROW)

def process_robot(curr_line: str):
    p,v = curr_line.split(' ')
    p_coords = p.split('p=')[1].split(',')
    v_coords = v.split('v=')[1].split(',')

    return {
        'pos': {
            'col': int(p_coords[0]),
            'row': int(p_coords[1])
        },
        'velo': {
            'col': int(v_coords[0]),
            'row': int(v_coords[1])    
        }
    }

# print(process_robot('p=2,4 v=2,-3'))

def position_after_seconds(robot: dict[str, dict[str, int]], seconds: int):
    return {
        'col': (robot['pos']['col'] + seconds*robot['velo']['col'])%WIDTH,
        'row': (robot['pos']['row'] + seconds*robot['velo']['row'])%HEIGHT,
    }

# print(position_after_seconds(process_robot('p=2,4 v=2,-3'), 1))
# print(position_after_seconds(process_robot('p=2,4 v=2,-3'), 2))
# print(position_after_seconds(process_robot('p=2,4 v=2,-3'), 3))
# print(position_after_seconds(process_robot('p=2,4 v=2,-3'), 4))
# print(position_after_seconds(process_robot('p=2,4 v=2,-3'), 5))

def process_robots(file_path, seconds: int):
    unique_spots = set()
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = line.rstrip()
            robot = process_robot(curr_line)
            pos = position_after_seconds(robot, seconds)

            c = pos['col']
            r = pos['row']

            key = f"{c}-{r}"
            
            unique_spots.add(key)

    return unique_spots

# quads = process_robots('../input/sample.txt')

seconds = 0
max_unique_spots = 0
while True:
    seconds+=1
    unique_spots = process_robots('../input/full.txt', seconds)
    if (len(unique_spots) > max_unique_spots):
        max_unique_spots = len(unique_spots)
        print('seconds', seconds)
        print('max spots: ', max_unique_spots)
        if max_unique_spots == 500:
            break
    
