# Approach build map of number -> set of numbers that can't appear later

# build a set of forbidden later pages
# if a page you are checking is in the set, bail
# if not, add those forbidden to the sets (set.update)

import functools

def add_rules(line: str, rules_bwd: dict[str, set[str]], rules_fwd: dict[str, set[str]]):
    early_page, later_page = line.rstrip().split('|')
    # print(page, banned_page)
    # convert to ints
    # pairs = list(map(int,pairs))
    if later_page in rules_bwd:
        rules_bwd[later_page].add(early_page)
    else:
        rules_bwd[later_page] = {early_page}

    if early_page in rules_fwd:
        rules_fwd[early_page].add(later_page)
    else:
        rules_fwd[early_page] = {later_page}

def is_valid_level(line:str, rules_bwd: dict[str, set[str]], rules_fwd: dict[str, set[str]]):
    level_list = line.rstrip().split(',')

    visited_pages: set[str] = set()
    for page in level_list:
        
        if page in rules_fwd:
            forward_rules = rules_fwd[page]
            for visited_page in visited_pages:
                if visited_page in forward_rules:
                    return False


            # print('early_pages', early_pages)
            # for early_page in early_pages:
            #     if early_page not in visited_pages:
            #         return 0
        visited_pages.add(page)

    return True


def sort_by_rules(rules_fwd: dict[str, set[str]], rules_bwd: dict[str, set[str]]):
    def inner_sort(a: str,b: str):

        # print('a', a)
        # print('b', b)
        # print(rules_fwd)

        if a in rules_fwd and b in rules_fwd[a]:
            return -1
        if a in rules_bwd and b in rules_bwd[a]:
            return 1
        return 0

    return inner_sort
    
    

def fix_level(line:str, rules_bwd: dict[str, set[str]], rules_fwd: dict[str, set[str]]):
    level_list = line.rstrip().split(',')

    print(level_list)
    fixed_level = sorted(level_list, key=functools.cmp_to_key(sort_by_rules(rules_fwd, rules_bwd)))
    print(fixed_level)


    return fixed_level

def read_file(file_path):

    tally = 0
    is_evaluating_levels = False
    rules_fwd: dict[str, set[str]] = {}
    rules_bwd: dict[str, set[str]] = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                is_evaluating_levels = True
                # print('fwd', rules_fwd)
                # print('bwd', rules_bwd)
                continue
            
            if is_evaluating_levels:
                if not is_valid_level(line, rules_bwd, rules_fwd):
                    fixed_level = fix_level(line, rules_bwd, rules_fwd)
                    tally+= int(fixed_level[len(fixed_level)//2])
            else:
                add_rules(line, rules_bwd, rules_fwd)

            
    return tally


rules = read_file('../input/full.txt')

print(rules)


