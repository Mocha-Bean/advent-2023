infile = open("day 9/input.txt", 'r', encoding="utf8")
sum = 0

def diffs(list):
    n = len(list)
    difflist = []
    for i in range(n-1):
        diff = list[i+1] - list[i]
        difflist.append(diff)
    return difflist

def allzeros(list):
    # returns True if 'list' is all zeros, otherwise False
    for value in list:
        if value != 0:
            return False
            break
    return True

def extrapolate(derivs):
    order = len(derivs)-1
    extrap = 0
    while order > 0:
        extrap = derivs[order-1][-1] + extrap
        order -= 1
    return extrap

for line in infile:
    history_str = line.split()
    history = []
    for str in history_str:
        history.append(int(str))
    # print(history)
    derivatives = []
    derivatives.append(history)
    order = 0
    while True:
        order += 1
        # get diffs and append to the list of derivatives
        derivatives.append(diffs(derivatives[order-1]))
        # print(derivatives[order])
        if allzeros(derivatives[order]):
            break
    extrap = extrapolate(derivatives)
    sum += extrap

print(sum)
    