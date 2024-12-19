# Approach

def process_instruction(instruction: int, l_operand: int, output: list[int], register):

    c_operand = l_operand

    if l_operand == 4:
        c_operand = register['a']
    elif l_operand == 5:
        c_operand = register['b']
    elif l_operand == 6:
        c_operand = register['c']

    if instruction == 0:
        val = register['a'] // pow(2, c_operand)
        register['a'] = val
    elif instruction == 1:
        val = register['b'] ^ l_operand
        register['b'] = val
    elif instruction == 2:
        val = c_operand %8
        register['b'] = val
    elif instruction == 3:
        if register['a'] != 0:
            return l_operand
    elif instruction == 4:
        val = register['b'] ^ register['c']
        register['b'] = val
    elif instruction == 5:
        val = c_operand%8
        output.append(val)
    elif instruction == 6:
        val = register['a'] // pow(2, c_operand)
        register['b'] = val
    elif instruction == 7:
        val = register['a'] // pow(2, c_operand)
        register['c'] = val

    return -1


def run_program(register: dict[str, int], program: list[int]):
    output: list[int] = []
    i = 0
    while i < len(program):
    
        instruction = program[i]
        operand = program[i+1]
        jump = process_instruction(instruction, operand, output, register)
        if jump == -1:
            i+= 2
        else:
            i = jump

    return output

def process_input(file_path: str):
    register = {
        'a': 0,
        'b': 0,
        'c': 0
    }
    program = []
    line_num =0
    with open(file_path, 'r') as file:
        for line in file:
            if line_num%6 == 0:
                register['a'] = int(line.split('Register A: ')[1])
            elif line_num%6 == 1:
                register['b'] = int(line.split('Register B: ')[1])
            elif line_num%6 == 2:
                register['c'] = int(line.split('Register C: ')[1])
            elif line_num%6 == 4:
                program_string = line.split('Program: ')[1]
                program = list(map(int, program_string.split(',')))
            
            line_num+= 1

    return register, program

# register, program = process_input('../input/sample.txt')
register, program = process_input('../input/full.txt')

print('register', register)
print('program', program)

output = run_program(register, program)

print('output', ','.join(str(x) for x in output))
