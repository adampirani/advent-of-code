# Approach build map of number -> set of numbers that can't appear later

# build a set of forbidden later pages
# if a page you are checking is in the set, bail
# if not, add those forbidden to the sets (set.update)

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

def evaluate_level(line:str, rules_bwd: dict[str, set[str]], rules_fwd: dict[str, set[str]]):
    level_list = line.rstrip().split(',')

    visited_pages: set[str] = set()
    # print(level_list)
    mid_page = level_list[len(level_list)//2]
    # print(mid_page)
    questionable_pages: set[str]
    for page in level_list:
        
        print('page', page)

        if page in rules_fwd:
            forward_rules = rules_fwd[page]
            for visited_page in visited_pages:
                if visited_page in forward_rules:
                    return 0


            # print('early_pages', early_pages)
            # for early_page in early_pages:
            #     if early_page not in visited_pages:
            #         return 0
        visited_pages.add(page)

    return int(mid_page)

def read_file(file_path):

    tally = 0
    is_evaluating_levels = False
    rules_fwd: dict[str, set[str]] = {}
    rules_bwd: dict[str, set[str]] = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                is_evaluating_levels = True
                print('fwd', rules_fwd)
                print('bwd', rules_bwd)
                continue
            
            if is_evaluating_levels:
                tally+= evaluate_level(line, rules_bwd, rules_fwd)
            else:
                add_rules(line, rules_bwd, rules_fwd)

            
    print(rules_fwd)

    return tally


rules = read_file('../input/full.txt')

print(rules)


