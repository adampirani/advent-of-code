# Approach

# get a map
# find all locations for each letter (dict)

def is_coord_valid(coord: dict[str, int], max_col: int, max_row: int):

    return (coord['r'] in range(0, max_row) and
            coord['c'] in range(0, max_col))



def add_anti_nodes(antennas: dict[str,list[dict[str,str]]] , blank_matrix: list[list[str]]):
    anti_node_coords = set()
    max_col = len(blank_matrix)
    max_row = len(blank_matrix[0])
    print('maxr', max_row)
    for char, coords_list in antennas.items():
        print(char, coords_list)
        num_coords = len(coords_list)
        for i in range(num_coords):
            coord = coords_list[i]
            print('coord', coord)
            for j in range(i + 1, num_coords):
                other_coord = coords_list[j]
                print('other_coord', other_coord)
                row_dist = other_coord['r'] - coord['r']
                col_dist = other_coord['c'] - coord['c']

                new_coord_1 = {
                    'r': coord['r'],
                    'c': coord['c']
                }

                while is_coord_valid(new_coord_1,  max_col, max_col):
                    anti_node_coords.add(f"{new_coord_1['r']}-{new_coord_1['c']}")
                    new_coord_1 = {
                        'r': new_coord_1['r'] - row_dist,
                        'c': new_coord_1['c'] - col_dist
                    }

                new_coord_2 = {
                    'r': other_coord['r'],
                    'c': other_coord['c']
                }
                
                while is_coord_valid(new_coord_2,  max_col, max_col):
                    anti_node_coords.add(f"{new_coord_2['r']}-{new_coord_2['c']}")
                    new_coord_2 = {
                        'r': new_coord_2['r'] + row_dist,
                        'c': new_coord_2['c'] + col_dist
                    }

                print(anti_node_coords)
                
                # print(anti_node_coords)
                # print('r_d', row_dist)
                # print('c_d', col_dist)

    return anti_node_coords     


def read_file_two_d_array(file_path):

    blank_matrix: list[list[str]] = []
    antenna_locations: dict[str,list[dict[str,str]]] = dict()
    row = 0
    with open(file_path, 'r') as file:
        for line in file:
            blank_matrix_row: list[str] = []
            curr_line = list(line.rstrip())

            for col in range(len(curr_line)):
                blank_matrix_row.append('.')
                char = curr_line[col]
                if char != '.':
                    coords = {'r': row, 'c': col}
                    if char in antenna_locations:
                        antenna_locations[char].append(coords)
                    else:
                        antenna_locations[char] = [coords]

            blank_matrix.append(blank_matrix_row)
            row+= 1
    return antenna_locations, blank_matrix

antennas, blank_matrix = read_file_two_d_array('../input/full.txt')

anti_node_matrix = add_anti_nodes(antennas, blank_matrix)

print(len(anti_node_matrix))

# print('antennas', antennas)
# print('blank', blank)

