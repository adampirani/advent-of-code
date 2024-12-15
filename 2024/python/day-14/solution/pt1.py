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

def process_robots(file_path):
    quads = [
        [],
        [],
        [],
        []
    ]
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = line.rstrip()
            robot = process_robot(curr_line)
            pos = position_after_seconds(robot, SECONDS)

            c = pos['col']
            r = pos['row']

            key = f"{c}-{r}"
            if r != INVALID_ROW and c != INVALID_COL:

                if r < INVALID_ROW:
                    if c < INVALID_COL:
                        quads[0].append(key)
                    else:
                        quads[1].append(key)
                else:
                    if c < INVALID_COL:
                        quads[2].append(key)
                    else:
                        quads[3].append(key)

    return quads

# quads = process_robots('../input/sample.txt')
quads = process_robots('../input/full.txt')

safety_factor = 1

for quad in quads:
    safety_factor*= len(quad)


print('safety factor: ', safety_factor)
print('too high: ', 223527360)
