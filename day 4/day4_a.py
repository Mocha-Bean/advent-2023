infile = open("day 4/input.txt", 'r', encoding="utf8")
sum = 0

for line in infile:
    value = 0
    after_colon = line.split(':')
    sections = after_colon[1].split('|')
    winning = sections[0].split()
    have = sections[1].split()
    for number in winning:
        if number in have:
            if(value == 0):
                value = 1
            else:
                value = value * 2
    sum += value

print(sum)