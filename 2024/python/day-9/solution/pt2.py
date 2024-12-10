# Approach

import functools

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.rstrip()

def create_blocks_and_gaps(disk_map: str):
    blocks: list[int|str] = list()
    gaps = {}

    is_file = True
    file_count=0
    for i in range(len(disk_map)):
        char = disk_map[i]
        num = int(char)

        if not is_file:
            if num in gaps:
                gaps[num].append(len(blocks))
            else:
                gaps[num] = [len(blocks)]

        for j in range(0,num):
            if is_file:
                blocks.append(file_count)
            else:
                blocks.append('.')

        if is_file:
            file_count+= 1
            
        is_file = not is_file

    gaps_array = []
    for key in gaps.keys():
        gaps_array.append({
            'size': key,
            'places': gaps[key]
        })

    return blocks, gaps_array

def calc_len(blocks: list[int|str], r: int):

    block_id = blocks[r]
    # print('cal len block_id:', block_id)
    length = 1
    idx = r - 1

    # print('spot before', blocks[idx])
    while blocks[idx] == block_id:
        idx-=1
        length+=1

    return length

def sort_by_first_place(gap_a: dict, gap_b:dict):
    places_a = gap_a['places']
    places_b = gap_b['places']

    if len(places_a) == 0:
        return 1
    if len(places_b) == 0:
        return -1
    

    
    return places_a[0]-places_b[0]

def find_space(length: int, max: int, gaps: dict):

    # print('find_space')
    # print('length', length)
    # print('max', max)
    # print('gaps', gaps)


    idx = -1
    new_len = 0
    for gap in gaps:
        places = gap['places']
        size = gap['size']
        if len(places) == 0:
            continue
        
        if places[0] + length > max:
            return -1, gaps
        
        if size < length:
            continue

        idx = places.pop(0)
        new_len = size - length
        break

    # print('found idx', idx)
    # print('new_len', new_len)

    if new_len > 0:
        new_pos = idx + length
        found_gap = False
        for gap in gaps:
            size = gap['size']
            if size == new_len:
                gap['places'].append(new_pos)
                gap['places'].sort()
                found_gap = True
                break
        if not found_gap:
            gaps.append({
                'size': new_len,
                'places': [new_pos]
            })

    gaps = sorted(gaps, key=functools.cmp_to_key(sort_by_first_place))
    
    return idx, gaps
    

def process_blocks(blocks: list[int|str], gaps: dict):
    r = len(blocks) - 1

    while blocks[r] == '.':
        r-= 1

    curr_id = int(blocks[r])

    while curr_id > 0:
        # print('curr_id', curr_id)

        if (r < 0):
            return

        while blocks[r] == '.' or blocks[r] > curr_id:
            r-=1
            if (r < 0):
                return
        # print('found_id: ', blocks[r])
        if blocks[r] != '.' and blocks[r] != curr_id:
            r-=1
            continue
    
        length = calc_len(blocks, r)

        empty_space, gaps = find_space(length,r, gaps)
        # print('made new gaps', gaps)
        # print('empty space', empty_space)

        if empty_space != -1:
            for i in range(empty_space, empty_space+length):
                # print('i', i)
                # print('curr_id', curr_id)
                blocks[i] = curr_id
            for i in range(r, r-length, -1):
                blocks[i] = '.'
            # print('moved', blocks)
        
        curr_id-= 1

def calc_checksum(blocks: list[int|str]):
    total = 0

    for i in range(len(blocks)):
        if blocks[i] == '.':
            continue
        total+= blocks[i] * i

    return total


disk_map = read_file('../input/full.txt')

# print(disk_map)

blocks, gaps = create_blocks_and_gaps(disk_map)

# print('blocks: ', blocks)
# print('gaps: ', gaps)
# print('blocks-len: ', len(blocks))

process_blocks(blocks, gaps)

# print('processed_blocks', blocks)

checksum = calc_checksum(blocks)

print('checksum', checksum)
# print('bad answer: ', 633859)
# print('bad answer: ', 6362076831426)
# print('bad answer: ', 6254526476832)
