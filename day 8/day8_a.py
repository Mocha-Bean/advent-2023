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

line = infile.readline()
for char in line:
    if char == 'L':
        dirs.append(0)
    elif char == 'R':
        dirs.append(1)

# skip blank line
infile.readline()

for i, line in enumerate(infile):
    label = line[0:3]
    left = line[7:10]
    right = line[12:15]
    labels.append(label)
    init_nodes.append((left, right))

for tuple in init_nodes:
    left_index = labels.index(tuple[0])
    right_index = labels.index(tuple[1])
    nodes.append((left_index, right_index))

AAA = labels.index("AAA")
ZZZ = labels.index("ZZZ")
location = AAA
steps = 0

# it's traversin' time
while location != ZZZ:
    for direction in dirs:
        location = nodes[location][direction]
        steps += 1

print(steps)