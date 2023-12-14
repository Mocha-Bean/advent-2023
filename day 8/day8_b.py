import math

infile = open("day 8/input.txt", 'r', encoding="utf8")
# list of left/right integer tuples
nodes = []
# list of string tuples, to be converted into integer tuples
init_nodes = []
# list of labels, so we can associate three-letter names with appropriate
# incides into the nodes[] list
labels = []
# list of left/right directions, where 0=left and 1=right
dirs = []
# list of nodes ending in A
starts = []
# list of nodes ending in Z
ends = []

line = infile.readline()
for char in line:
    if char == 'L':
        dirs.append(0)
    elif char == 'R':
        dirs.append(1)

# total number of directions
n_dirs = len(dirs)

# skip blank line
infile.readline()

for i, line in enumerate(infile):
    label = line[0:3]
    left = line[7:10]
    right = line[12:15]
    labels.append(label)
    init_nodes.append((left, right))
    if label[2] == 'A':
        starts.append(i)
    elif label[2] == 'Z':
        ends.append(i)

for tuple in init_nodes:
    left_index = labels.index(tuple[0])
    right_index = labels.index(tuple[1])
    nodes.append((left_index, right_index))

# current location of each ghost
locations = starts
steps = []

# find how many steps to reach an end point from each starting point
for i in range(len(starts)):
    steps.append(0)
    while locations[i] not in ends:
        for direction in dirs:
            locations[i] = nodes[locations[i]][direction]
            steps[i] += 1

# find least common multiple of each number of steps
print(math.lcm(*steps))