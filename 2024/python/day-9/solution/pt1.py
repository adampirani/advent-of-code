# Approach


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.rstrip()

def create_blocks(disk_map: str):
    blocks: list[int|str] = list()

    is_file = True
    file_count=0
    for char in disk_map:
        num = int(char)

        for i in range(0,num):
            if is_file:
                blocks.append(file_count)
            else:
                blocks.append('.')

        if is_file:
            file_count+= 1
        is_file = not is_file

    print('filecount: ', file_count)
    return blocks

def process_blocks(blocks: list[int|str]):
    l = 0
    r = len(blocks) - 1
    while l < r:
        while blocks[l] != '.':
            l+= 1
        while blocks[r] == '.':
            r-= 1

        blocks[l] = blocks[r]
        blocks[r] = '.'
        l+=1
        r-=1

def calc_checksum(blocks: list[int|str]):
    total = 0

    for i in range(len(blocks)):
        if blocks[i] == '.':
            return total
        total+= blocks[i] * i

    return total


disk_map = read_file('../input/full.txt')

# print(disk_map)

blocks = create_blocks(disk_map)
# print('blocks-len: ', len(blocks))
print('blocks: ', blocks)

process_blocks(blocks)

# print('processed_blocks', blocks)

checksum = calc_checksum(blocks)

print(checksum)

