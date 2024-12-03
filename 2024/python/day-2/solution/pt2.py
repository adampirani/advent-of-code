
def is_change_safe(delta: int):
    if delta == 0:
        return False
    
    return abs(delta) <= 3

def is_increasing(delta: int):
    return True if delta > 0 else False


def is_safe(levels: list[int]):
    first_increment = levels[1] - levels[0]
    if not is_change_safe(first_increment):
        # print('first change not safe: ', levels[1], levels[0] )
        return False
    
    is_first_increasing = is_increasing(first_increment)

    # print('is_first_increasing', is_first_increasing)

    for i in range(1, len(levels) - 1):
        increment = levels[i+1] - levels[i]
        # print('increment', increment)

        if is_increasing(increment) != is_first_increasing:

            # print('change of increase vs. decrease, abort')
            return False
        
        if not is_change_safe(increment):
            # print('change too big or no change, abort')
            return False
        
    return True

def any_level_variation_is_safe(levels: list[int]):
    for i in range(0, len(levels)):
        levels_without_index = levels.copy()
        del levels_without_index[i]

        if is_safe(levels_without_index):
            # print('passed by removing index', i)
            return True
        
    # print('could not remove any')
    return False



def read_file(file_path):

    num_safe: int = 0

    with open(file_path, 'r') as file:
        for report in file:
            levels = report.rstrip().split()
            # convert to ints
            levels = list(map(int,levels))

            if is_safe(levels):
                num_safe += 1
            elif any_level_variation_is_safe(levels):
                num_safe += 1

    return num_safe

num_safe = read_file('../input/full.txt')

print(num_safe)

