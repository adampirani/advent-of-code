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

    all_combos = list(itertools.product('/-|', repeat=len(inputs_ints)-1))
    # print('all_combos', all_combos)

    for combo in all_combos:
        # print(combo)
        tally = total_int
        # print('tally: ', tally)
        # print('len(combo): ', len(combo))
        failed = False
        for i in range(len(combo)):
            operator = combo[i]
            # print('tally', tally)
            # print('operator', operator)
            # print('checking w/', inputs_ints[i])

            next_input = inputs_ints[i]

            if operator == '/':
                if tally%next_input != 0:
                    failed = True
                    break
                tally//= next_input
            elif operator== '-':
                if tally-next_input < 0:
                    failed = True
                    break
                tally-= next_input
            else:
                str_tally = str(tally)
                str_next_input = str(next_input)

                if len(str_tally) <= len(str_next_input):
                    failed=True
                    break

                # print('str_tally[-len(str_next_input):]', str_tally[-len(str_next_input):])
                if str_tally[-len(str_next_input):] != str_next_input:
                    failed = True
                    break
                # print('int(str_tally[0:len(str_next_input)])', int(str_tally[0:len(str_next_input)]))

                # print('attempted to un-concat',next_input, 'from', tally)
                tally = int(str_tally[:-len(str_next_input)])
                # print('result', tally)
                    

            # print('new tally: ', tally)

        if not failed and tally == inputs_ints[-1]:
            # print('passed')
            return True

    # print('failed')
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
