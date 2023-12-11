infile = open("day 5/input.txt", 'r', encoding="utf8")
# list containing seeds, or whatever they're mapped to
seeds = []
# list containing a boolean value indicating whether each seed has been mapped
located = []

for index, line in enumerate(infile):
    if index == 0:
        after_colon = line.split(':')
        seeds_str = after_colon[1].split()
        for str in seeds_str:
            seeds.append(int(str))
            located.append(False)
    elif len(line) == 1:
        # we've hit the end of a section, set each seed to unlocated
        located = [False] * len(seeds)
    elif line[0].isnumeric():
        # we're on a line with mappings
        mapping_str = line.split()
        mapping = []
        for str in mapping_str:
            mapping.append(int(str))
        offset = mapping[0] - mapping[1]
        for i, seed in enumerate(seeds):
            if located[i] == False:
                # calculate difference between seed and source range start
                diff = seed - mapping[1]
                if 0 <= diff < mapping[2]:
                    # seed is in source range, map it and mark it as located
                    seeds[i] += offset
                    located[i] = True

print(min(seeds))