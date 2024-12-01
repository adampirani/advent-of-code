
def read_file(file_path):
    left = []
    right = []
    with open(file_path, 'r') as file:
        for line in file:
            pairs = line.rstrip().split()
            # convert to ints
            pairs = list(map(int,pairs))
            left.append(pairs[0])
            right.append(pairs[1])
    return left, right

left, right = read_file('../input/full.txt')

r_freq = {}

for i in right:
    if i not in r_freq:
        r_freq[i] = 0
    r_freq[i]+= 1;

# print(r_freq)

similarity_score = 0
for i in left:
    if i in r_freq:
        similarity_score+= r_freq[i]*i  
    # print(similarity_score)

print(similarity_score)


