import re

infile = open("day 3/input.txt", 'r', encoding="utf8")
sum = 0
schematic = []
numbers = []
# dict with key being coords of asterisk and value being a list of matches for
# adjacent numbers
gears = {}

# load input file into a list of strings
for index, line in enumerate(infile):
    schematic.append(line.replace('\n','')) # remove newline

for line in schematic:
    numbers.append(re.finditer(r"\d+", line)) # apppend iterator to 'numbers' list

def checkchar(y, x, match):
    char = schematic[y][x]
    if char == '*':
        returnval = True
        if (y,x) not in gears:
            # add entry to dict with value being a list including match
            gears[(y,x)] = [match]
        else:
            if match not in gears[(y,x)]:
                gears[(y,x)].append(match)
    else:
        returnval = False
    return returnval

max_y = len(schematic) - 1
max_x = len(schematic[0]) - 1
for y, iterator in enumerate(numbers):
    # iterate over each match in line y
    for match in iterator:
        start = match.start()
        num_str = match.group(0)
        n = len(num_str)

        # iterate over each digit of the number and check adjacents
        for i in range(n):
            if(i == 0 and start > 0):
                # check left side
                if(y > 0):
                    # check top-left
                    if checkchar(y-1, start-1, match):
                        break # assuming a number cannot have multiple adjacent '*'
                # check mid-left
                if checkchar(y, start-1, match):
                    break
                if(y < max_y):
                    # check bottom-left
                    if checkchar(y+1, start-1, match):
                        break

            if(i == n-1 and start+i < max_x):
                # check right side
                if(y > 0):
                    # check top-right
                    if checkchar(y-1, start+n, match):
                        break
                # check mid-right
                if checkchar(y, start+n, match):
                    break
                if (y < max_y):
                    # check bottom-right
                    if checkchar(y+1, start+n, match):
                        break
            
            # check above and below
            if(y > 0):
                # check above
                if checkchar(y-1, start+i, match):
                    break
            if(y < max_y):
                # check below
                if checkchar(y+1, start+i, match):
                    break

for coords in gears:
    if len(gears[coords]) == 2:
        # has exactly 2 adjacent part numbers
        num0 = int(gears[coords][0].group(0))
        num1 = int(gears[coords][1].group(0))
        sum += num0 * num1

print(sum)