import re

def getdigit(s):
    if s.isnumeric():
        return int(s)
    else:
        match s:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9

infile = open("day 1/input.txt", 'r', encoding="utf8")
sum = 0

for line in infile:
    digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    digit0 = getdigit(digits[0])
    digit1 = getdigit(digits[-1])
    value = 10*digit0 + digit1
    sum += value

print(sum)