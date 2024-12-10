# Approach

# For each line find all combos of divide & subtract actions
# Stop this path if
# any division that isn't an int
# any subtraction that goes negative
# doesn't end
# 
import itertools

def is_valid(total_int: int, inputs_ints: list[int]):

    # print('goal: ', total_int)
    # print('input ints: ', inputs_ints)

    inputs_ints.reverse()

    all_combos = list(itertools.product('/-', repeat=len(inputs_ints)-1))
    # print('all_combos', all_combos)

    for combo in all_combos:
        # print(combo)
        tally = total_int
        # print('tally: ', tally)
        # print('len(combo): ', len(combo))
        for i in range(len(combo)):
            operator = combo[i]
            # print('operator', operator)
            idx = i

            # print('checking w/', inputs_ints[idx])

            if operator == '/':
                tally/= inputs_ints[idx]
            else:
                tally-= inputs_ints[idx]

            # print('new tally: ', tally)

        if tally == inputs_ints[-1]:
            return True

    return False

def evaluate_line(curr_line: str):
    total, inputs = curr_line.split(': ')
    total_int = int(total)
    inputs_ints = list(map(int,inputs.split(' ')))

    if is_valid(total_int, inputs_ints):
        return total_int
    
    return 0

def process_equations(file_path):
    tally = 0
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = line.rstrip()
            if curr_line != '':
                tally+= evaluate_line(curr_line)

    return tally

total = process_equations('../input/full.txt')

print(total)

