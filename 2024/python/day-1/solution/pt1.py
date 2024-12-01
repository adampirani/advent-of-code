
def read_file(file_path):

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

l, r = read_file('../input/full.txt')

l.sort()
r.sort()
print(l)
print(r)

diffs = []
for i in range(0, len(l)):
    diffs.append(abs(l[i] - r[i]))

print(diffs)

total_diffs = 0

for x in diffs:
    total_diffs+= x

print(total_diffs)

