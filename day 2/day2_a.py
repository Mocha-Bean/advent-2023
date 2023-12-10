import re

infile = open("day 2/input.txt", 'r', encoding="utf8")
sum = 0

for index, line in enumerate(infile):
    game = index + 1
    sections = line.split(':')
    pulls = sections[1].split(';')
    possible = True

    for pull in pulls:
        red_match = re.search(r"\d+(?= red)", pull)
        if(red_match):
            red = int(red_match.group(0))
        else:
            red = 0
        if red > 12:
            possible = False
        
        green_match = re.search(r"\d+(?= green)", pull)
        if(green_match):
            green = int(green_match.group(0))
        else:
            green = 0
        if green > 13:
            possible = False

        blue_match = re.search(r"\d+(?= blue)", pull)
        if(blue_match):
            blue = int(blue_match.group(0))
        else:
            blue = 0
        if blue > 14:
            possible = False
    if possible:
        sum += game

print(sum)