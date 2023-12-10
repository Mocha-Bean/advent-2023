import re

infile = open("day 2/input.txt", 'r', encoding="utf8")
sum = 0

for index, line in enumerate(infile):
    sections = line.split(':')
    pulls = sections[1].split(';')
    min_r = 0
    min_g = 0
    min_b = 0

    for pull in pulls:
        red_match = re.search(r"\d+(?= red)", pull)
        if(red_match):
            red = int(red_match.group(0))
        else:
            red = 0
        if red > min_r:
            min_r = red
        
        green_match = re.search(r"\d+(?= green)", pull)
        if(green_match):
            green = int(green_match.group(0))
        else:
            green = 0
        if green > min_g:
            min_g = green

        blue_match = re.search(r"\d+(?= blue)", pull)
        if(blue_match):
            blue = int(blue_match.group(0))
        else:
            blue = 0
        if blue > min_b:
            min_b = blue
    
    power = min_r * min_g * min_b
    sum += power

print(sum)