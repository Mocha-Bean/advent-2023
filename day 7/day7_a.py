infile = open("day 7/input.txt", 'r', encoding="utf8")
hands = []
bids = []

def handtype(str):
    # returns the type of hand
    appearances = {}
    for char in str:
        if char not in appearances:
            appearances[char] = 1
        else:
            appearances[char] += 1
    n = len(appearances)
    match n:
        case 1:
            # five of a kind
            return 6
        case 2:
            # get the letter with the most appearances
            c = max(appearances, key=appearances.get)
            max_c = appearances[c]
            if max_c == 4:
                # four of a kind
                return 5
            else:
                # full house
                return 4
        case 3:
            c = max(appearances, key=appearances.get)
            max_c = appearances[c]
            if max_c == 3:
                # three of a kind
                return 3
            else:
                # two pair
                return 2
        case 4:
            # one pair
            return 1
        case 5:
            # high card
            return 0
        
def numberize(c):
    # turn a char from the hand into a number so that
    # it can be compared numerically
    if c.isnumeric():
        return int(c)
    else:
        match c:
            case 'T':
                return 10
            case 'J':
                return 11
            case 'Q':
                return 12
            case 'K':
                return 13
            case 'A':
                return 14

def better_hand(a, b):
    # return True if a is a better hand than b, otherwise False
    type_a = handtype(a)
    type_b = handtype(b)
    if type_a > type_b:
        return True
    elif type_a < type_b:
        return False
    else:
        # compares strength of each card in order until there's a difference
        for i in range(5):
            strength_a = numberize(a[i])
            strength_b = numberize(b[i])
            if strength_a > strength_b:
                return True
            elif strength_a < strength_b:
                return False
        # if we've made it here, the hands are identical, so it doesn't
        # matter what we return
        return True

def insert(i):
    # inserts hands[i] to where it belongs in the list (a la insert sort)
    while i > 0 and better_hand(hands[i-1], hands[i]):
        hands.insert(i-1, hands[i])
        bids.insert(i-1, bids[i])
        hands.pop(i+1)
        bids.pop(i+1)
        i -= 1

for i, line in enumerate(infile):
    sections = line.split()
    hands.append(sections[0])
    bids.append(int(sections[1]))
    insert(i)

sum = 0
for i in range(len(bids)):
    # the hands are sorted, so rank = i+1
    sum += (i+1) * bids[i]

print(sum)