# Approach

# Convert file into two-d array of strings
# move through array until an 'x' is found
# search all 8 directions for xmas, add 1 for each
#

def read_file_two_d_array(file_path):

    puzzle_matrix: list[list[str]] = []
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            puzzle_matrix.append(curr_line)
    return puzzle_matrix

def is_cross_mas(puzzle_matrix: list[list[str]], row_idx: int, col_idx: int):
    row_max = len(puzzle_matrix) - 1
    col_max = len(puzzle_matrix[0]) - 1 #assumes every row is same length
    iterators= [[[-1,-1], [1,1]], [[-1,1],[1,-1]]]

    for pairs in iterators:

        one_end_iter = pairs[0]
        other_end_iter = pairs[1]

        one_end_row = row_idx + one_end_iter[0]
        one_end_col = col_idx + one_end_iter[1]

        if one_end_row < 0 or one_end_row > row_max:
            return False
        
        if one_end_col < 0 or one_end_col > col_max:
            return False
        
        other_end_row = row_idx + other_end_iter[0]
        other_end_col = col_idx + other_end_iter[1]

        if other_end_row < 0 or other_end_row > row_max:
            return False
        
        if other_end_col < 0 or other_end_col > col_max:
            return False
        
        one_end_letter = puzzle_matrix[one_end_row][one_end_col]
        other_end_letter = puzzle_matrix[other_end_row][other_end_col]

        print('one_end_letter: ', one_end_letter)
        print('other_end_letter: ', other_end_letter)

        if not ((one_end_letter == 'M' and other_end_letter == 'S') or (one_end_letter == 'S' and other_end_letter == 'M')):
            return False

    return True

def process_matrix(puzzle_matrix: list[list[str]]):
    total = 0
    for row_idx in range(len(puzzle_matrix)):
        row = puzzle_matrix[row_idx]
        for col_idx in range(len(row)):
            if row[col_idx] != 'A':
                continue
            # only dealing with 'A'


            total+= 1 if is_cross_mas(puzzle_matrix, row_idx, col_idx) else 0

    return total


puzzle_matrix = read_file_two_d_array('../input/full.txt')

count = process_matrix(puzzle_matrix)

print(count)

