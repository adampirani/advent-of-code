def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def read_file_two_cols(file_path):

    left = []
    right = []
    with open(file_path, 'r') as file:
        for line in file:
            print(line.rstrip())
            pairs = line.rstrip().split()
            # convert to ints
            pairs = list(map(int,pairs))
            left.append(pairs[0])
            right.append(pairs[1])
    return left, right

def read_file_two_d_array(file_path):

    puzzle_matrix: list[list[str]] = []
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            puzzle_matrix.append(curr_line)
    return puzzle_matrix
