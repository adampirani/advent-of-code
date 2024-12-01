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
