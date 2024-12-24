# Approach build map of number -> set of numbers that can't appear later

def is_possible(pattern: str, passed_patterns: set[str], failed_patterns: set[str]):

    if pattern in passed_patterns:
        return True
    
    if pattern in failed_patterns:
        return False

    for i in range(1, len(pattern)):
        left = pattern[:i]
        right=pattern[i:]

        # print('pattern', pattern)
        # print('left', left)
        # print('right', right)

        if is_possible(left, passed_patterns, failed_patterns) and is_possible(right, passed_patterns, failed_patterns):
            passed_patterns.add(pattern)
            return True

    failed_patterns.add(pattern)
    return False
        


def get_possible_patterns(towels: set[str], patterns: list[str]):
    failed_patterns: set[str] = set()
    passed_patterns: set[str] = set()

    possible_patterns = []

    for towel in towels:
        passed_patterns.add(towel)

    for pattern in patterns:
        if is_possible(pattern, passed_patterns, failed_patterns):
            # print('possible pattern: ', pattern)
            possible_patterns.append(pattern)
        # else: 
            # print('IMpossible pattern: ', pattern)

    # print('failed: ', failed_patterns)
    # print('passed: ', passed_patterns)

    return possible_patterns

def read_file(file_path):

    is_getting_patterns = False
    towels: set[str] = set()
    patterns: list[str] = []

    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                is_getting_patterns = True
                continue
            
            if is_getting_patterns:
                patterns.append(line.rstrip())
            else:
                line_towels = line.rstrip().split(', ')
                for towel in line_towels:
                    towels.add(towel)

    return towels, patterns


towels, patterns = read_file('../input/sample.txt')
# towels, patterns = read_file('../input/full.txt')

# print(towels)
# print(patterns)

possible_patterns = get_possible_patterns(towels, patterns)

print(possible_patterns)


