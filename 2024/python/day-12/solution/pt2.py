# Approach

DIRECTION_INCREMENTS = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def read_file_two_d_array(file_path):

    garden: list[list[str]] = []
    with open(file_path, 'r') as file:
        for line in file:
            curr_line = list(line.rstrip())
            garden.append(curr_line)

    return garden

def get_coord_key(r: int, c:int):
    return f"{r}-{c}"

def get_region_for_space(space: str, warehouse: list[list[str]], r: int, c: int, visited_coords: set[str]):
    spaces_to_check = []
    spaces_to_check.append({
        'r': r,
        'c': c
    })
    region: list[dict[str, int]] = []
    max_row = len(warehouse)
    max_col = len(warehouse[0])
    
    while len(spaces_to_check) > 0:
        checking_space = spaces_to_check.pop()
        space_r = checking_space['r']
        space_c = checking_space['c']
        coord_key = get_coord_key(space_r, space_c)
        if coord_key in visited_coords:
            continue
        visited_coords.add(get_coord_key(space_r,space_c))
        region.append(checking_space)
        for direction in DIRECTION_INCREMENTS:
            row = space_r + direction[0]
            col = space_c + direction[1]
            if row in range(0, max_row) and col in range(0, max_col):
                key = get_coord_key(row, col)
                if key not in visited_coords:
                    if warehouse[row][col] == space:
                        spaces_to_check.append({'r': row, 'c': col})

    return region

def get_regions_from_garden(warehouse: list[list[str]]):
    regions: list[list[dict[str, int]]] = []
    visited_coords: set[str] = set()
    for r in range(len(warehouse)):
        row = warehouse[r]
        for c in range(len(row)):
            if get_coord_key(r,c) in visited_coords:
                continue

            space = warehouse[r][c]

            region = get_region_for_space(space, warehouse, r, c, visited_coords)
            regions.append(region)

    return regions

def calc_perimeter(region: list[dict[str, int]], warehouse: list[list[str]]):
    max_row = len(warehouse)
    max_col = len(warehouse[0])
    
    # rows with list of cols
    top_edges: dict[int, list[int]] = {}
    bottom_edges: dict[int, list[int]] = {}

    # cols with list of rows
    left_edges: dict[int, list[int]] = {}
    right_edges: dict[int, list[int]] = {}

    all_edges = [top_edges, bottom_edges, left_edges, right_edges]
    edge_keys = {
        'top': 0,
        'bottom': 1,
        'left': 2,
        'right': 3
    }
    for space_loc in region:
        space_r = space_loc['r']
        space_c = space_loc['c']
        space_val = warehouse[space_r][space_c]

        for direction in DIRECTION_INCREMENTS:
            neighbor_r = space_r + direction[0]
            neighbor_c = space_c + direction[1]
            edge_key = None

            if neighbor_r < 0: #top edge
                edge_key = edge_keys['top']
            elif neighbor_r == max_row: # bottom edge
                edge_key = edge_keys['bottom']
            elif neighbor_c < 0: #left edge
                edge_key = edge_keys['left']
            elif neighbor_c == max_col: #right edge
                edge_key = edge_keys['right']
            else:
                neighbor_val = warehouse[neighbor_r][neighbor_c]
                if neighbor_val != space_val:
                    if direction[0] == -1: #top edge
                        edge_key = edge_keys['top']
                    elif direction[0] == 1: #bottom edge
                        edge_key = edge_keys['bottom']
                    elif direction[1] == -1: #left edge
                        edge_key = edge_keys['left']
                    elif direction[1] == 1: #right edge
                        edge_key = edge_keys['right']
            
            if edge_key == edge_keys['top']:
                if neighbor_r in top_edges:
                    top_edges[neighbor_r].append(neighbor_c)
                else:
                    top_edges[neighbor_r] = [neighbor_c]
            if edge_key == edge_keys['bottom']:
                if neighbor_r in bottom_edges:
                    bottom_edges[neighbor_r].append(neighbor_c)
                else:
                    bottom_edges[neighbor_r] = [neighbor_c]
            if edge_key == edge_keys['left']:
                if neighbor_c in left_edges:
                    left_edges[neighbor_c].append(neighbor_r)
                else:
                    left_edges[neighbor_c] = [neighbor_r]
            if edge_key == edge_keys['right']:
                if neighbor_c in right_edges:
                    right_edges[neighbor_c].append(neighbor_r)
                else:
                    right_edges[neighbor_c] = [neighbor_r]

    edge_num = 0
    perimeter = 0
    for edge in all_edges:
        edge_num+=1
        # print('edge num: ', edge_num)
        # print('edge: ', edge)
        for key in edge:
            edge[key].sort()

            # print('edge key', edge[key])
            # count consecutive rows/cols
            current_r_c = edge[key][0]
            num_edges = 1
            for row_col in edge[key][1:]:
                if row_col != current_r_c + 1:
                    num_edges+=1
                current_r_c = row_col
            # print('num_edges: ', num_edges)
            perimeter+= num_edges

    return perimeter

        

def price_all_regions(regions: list[list[dict[str, int]]], garden: list[list[str]]):
    total = 0
    count = 0
    for region in regions:
        count+=1
        area = len(region)
        perimeter = calc_perimeter(region, garden)

        # print('region #', count)
        # print('area', area)
        # print('perimeter', perimeter)

        total+= area * perimeter

    return total

# garden = read_file_two_d_array('../input/sample.txt')
garden = read_file_two_d_array('../input/full.txt')

regions = get_regions_from_garden(garden)

# print(len(regions))
# for i in range(len(regions)):
#     print('region#: ', i)
#     print('area: ', len(regions[i]))

total_price = price_all_regions(regions, garden)

print(total_price)

