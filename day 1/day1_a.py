import re

infile = open("day 1/input.txt", 'r', encoding="utf8")
sum = 0

for line in infile:
    digits = re.findall(r"\d", line)
    value_str = digits[0] + digits[-1]
    value = int(value_str)
    print(value)
    sum += value

print(sum)