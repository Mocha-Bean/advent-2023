infile = open("day 4/input.txt", 'r', encoding="utf8")
# starting number of cards
initsum = 208
# array of ones for initial quantity of each card
quantity = [1] * initsum
sum = initsum

for index, line in enumerate(infile):
    n = 0
    after_colon = line.split(':')
    sections = after_colon[1].split('|')
    winning = sections[0].split()
    have = sections[1].split()
    for number in winning:
        if number in have:
            n += 1
    for i in range(n):
        if index+i+1 < initsum:
            # add the quantity of this card to the next n cards
            quantity[index+i+1] += quantity[index]
            sum += quantity[index]

print(sum)