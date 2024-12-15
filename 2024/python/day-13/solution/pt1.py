# Approach

import re

def process_button(curr_line: str):
    button_line = re.split(r'Button [A|B]: ', curr_line)
    x,y = button_line[1].split(', ')
    return {
        'x': int(x[2:]),
        'y': int(y[2:])
    }

# print(process_button('Button A: X+94, Y+34'))
# print(process_button('Button B: X+94, Y+34'))

def process_prize(curr_line: str):
    prize_line = curr_line.split('Prize: ')
    x,y = prize_line[1].split(', ')
    return {
        'x': int(x[2:]),
        'y': int(y[2:])
    }

# print(process_prize('Prize: X=8400, Y=5400'))

#  
# x: a*94 + b*22 = 8400
# y: a*34 + b*67 = 5400
# --> 
# x*34: 3196a + 748b = 285600
# y*94: 3196a + 6298b = 507600

# 5550b = 222,000  --> b = 40
# a -> 80

def min_tokens_for_equation(eq: dict[str, int]):
    b_presses = (eq['prize']['x'] * eq['a']['y'] - eq['prize']['y']*eq['a']['x']) / (eq['b']['x'] * eq['a']['y'] - eq['b']['y'] * eq['a']['x'])
    
    if b_presses != int(b_presses):
        return 0

    a_presses = (eq['prize']['x'] - eq['b']['x'] * b_presses) / eq['a']['x']

    # print('a_presses', a_presses)
    # print('b_presses', b_presses)

    return a_presses*3 + b_presses

def process_equations(file_path):
    equations = []
    line_num =0
    tokens_spent = 0
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = line.rstrip()
            if line_num%4 == 0:
                equations.append(
                    {
                        'a': process_button(curr_line),
                        'b': None,
                        'prize': None
                    }
                )
            elif line_num%4 == 1:
                equations[-1]['b'] = process_button(curr_line)
            elif line_num%4 == 2:
                equations[-1]['prize'] = process_prize(curr_line)
            elif line_num%4 == 3:
                tokens_spent += min_tokens_for_equation(equations[-1])
            
            line_num+= 1

    return tokens_spent

# total = process_equations('../input/sample.txt')
total = process_equations('../input/full.txt')

print(total)

