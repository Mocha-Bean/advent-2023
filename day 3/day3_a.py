import re

infile = open("day 3/input.txt", 'r', encoding="utf8")
sum = 0
schematic = []
numbers = []

# load input file into a list of strings
for index, line in enumerate(infile):
    schematic.append(line.replace('\n','')) # remove newline

for line in schematic:
    numbers.append(re.finditer(r"\d+", line)) # apppend iterator to 'numbers' list

max_y = len(schematic) - 1
max_x = len(schematic[0]) - 1
for y, iterator in enumerate(numbers):
    # iterate over each match in line y
    for match in iterator:
        start = match.start()
        num_str = match.group(0)
        n = len(num_str)
        ispart = False

        # iterate over each digit of the number and check adjacents
        for i in range(n):
            if(i == 0 and start > 0):
                # check left side
                if(y > 0):
                    # check top-left
                    char = schematic[y-1][start-1]
                    if char != '.':
                        ispart = True
                        break
                # check mid-left
                char = schematic[y][start-1]
                if char != '.':
                    ispart = True
                    break
                if(y < max_y):
                    # check bottom-left
                    char = schematic[y+1][start-1]
                    if char != '.':
                        ispart = True
                        break

            if(i == n-1 and start+i < max_x):
                # check right side
                if(y > 0):
                    # check top-right
                    char = schematic[y-1][start+n]
                    if char != '.':
                        ispart = True
                        break
                # check mid-right
                char = schematic[y][start+n]
                if char != '.':
                    ispart = True
                    break
                if (y < max_y):
                    # check bottom-right
                    char = schematic[y+1][start+n]
                    if char != '.':
                        ispart = True
                        break
            
            # check above and below
            if(y > 0):
                # check above
                char = schematic[y-1][start+i]
                if char != '.':
                    ispart = True
                    break
            if(y < max_y):
                # check below
                char = schematic[y+1][start+i]
                if char != '.':
                    ispart = True
                    break

        if ispart:
            sum += int(num_str)

print(sum)