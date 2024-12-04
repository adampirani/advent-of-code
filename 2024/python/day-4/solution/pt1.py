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

def count_eight_directions(puzzle_matrix: list[list[str]], row_idx: int, col_idx: int):
    
    # assume all directions work, deduct count for each direction that fails
    count = 8

    row_max = len(puzzle_matrix) - 1
    col_max = len(puzzle_matrix[0]) - 1 #assumes every row is same length
    eight_iterators= [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1],[1,0], [1,1]]
    next_three_letters = ['M','A','S']

    for iterator in eight_iterators:

        curr_row = row_idx
        curr_col = col_idx
        for i in range(len(next_three_letters)):
            curr_row += iterator[0]
            curr_col += iterator[1]
            if curr_row < 0 or curr_row > row_max:
                count-=1
                break
            if curr_col < 0 or curr_col > col_max:
                count-=1
                break
            test_letter = puzzle_matrix[curr_row][curr_col]

            if test_letter != next_three_letters[i]:
                count-=1
                break        

    # print(count)
    
    return count

def process_matrix(puzzle_matrix: list[list[str]]):
    total = 0
    for row_idx in range(len(puzzle_matrix)):
        row = puzzle_matrix[row_idx]
        for col_idx in range(len(row)):
            if row[col_idx] != 'X':
                continue
            # only dealing with 'X'

            total+= count_eight_directions(puzzle_matrix, row_idx, col_idx)

    return total


puzzle_matrix = read_file_two_d_array('../input/full.txt')

print(puzzle_matrix)

count = process_matrix(puzzle_matrix)

print(count)

