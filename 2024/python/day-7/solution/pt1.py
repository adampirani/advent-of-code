# Approach

# For each line find all combos of divide & subtract actions
# Stop this path if
# any division that isn't an int
# any subtraction that goes negative
# doesn't end
# 
import math

def generate_operator_combos(num_operators: int):

    operator_combos: list[str] = list()

    return []

def is_valid(total_int: int, inputs_ints: list[int]):

    print('is valid total:', total_int)
    inputs_ints.reverse()
    print('is valid inputs_ints reversed:', inputs_ints)
    running_total = total_int
    visited_ops: list[str] = list()
    inputted_ints: list[int] = list()
    next_op = '-'

    loop_count = 0

    while len(visited_ops) < len(inputs_ints):
        loop_count+= 1
        if loop_count > 30:
            print('hit infinite')
            return False
        
        print('ttl: ', running_total)
        print('visited_ops: ', visited_ops)
        print('next_op: ', next_op)


        if len(visited_ops) == len(inputs_ints) - 1:
            print('reached max ops')
            if running_total == inputs_ints[-1]:
                print('REAL RETURN TRUE\n')
                return True
            undo_op = visited_ops[-1]
            if undo_op == '-':
                running_total+= inputted_ints.pop()
                visited_ops.pop()
                print('undo 1 minus', visited_ops)
                next_op = '/'
            else:
                # go back to the first '/' 
                while len(visited_ops) > 0 and visited_ops[-1] == '/':
                    visited_ops.pop()
                    running_total*= inputted_ints.pop()
                if len(visited_ops) == 0:
                    print('bailed out top!\n')
                    return False
                else:
                    next_op = '-'
            continue



        next_input = inputs_ints[len(visited_ops)]

        if next_op == '-':
            running_total-= next_input
            visited_ops.append('-')
            inputted_ints.append(next_input)
            # if negative, back out and try a divide instead
            if running_total < 0:
                running_total+= inputted_ints.pop()
                visited_ops.pop()
                next_op = '/'
        else:
            running_total/= next_input
            visited_ops.append('/')
            inputted_ints.append(next_input)

            if running_total.is_integer():
                running_total = running_total
                next_op = '-'
            else:
                while len(visited_ops) > 0 and visited_ops[-1] == '/':
                    visited_ops.pop()
                    running_total*= inputted_ints.pop()
                if len(visited_ops) == 0:
                    print('bailed out bottom2!\n')
                    return False
                # change one '-' to '/'
                visited_ops.pop()
                running_total+= inputted_ints.pop()


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

