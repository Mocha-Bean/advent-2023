infile = open("day 5/input.txt", 'r', encoding="utf8")
# list containing tuples of seeds (start, end) (inclusive)
seeds = []
# list containing tuples of destinations (start, end) (inclusive)
dests = []
# list of mappings for the current section
mappings = []

lines = infile.readlines()
last = len(lines)-1

for index, line in enumerate(lines):
    if index == 0:
        after_colon = line.split(':')
        seeds_str = after_colon[1].split()
        temp = 0
        for i, str in enumerate(seeds_str):
            if i % 2 == 1:
                seeds.append((temp, temp+int(str)-1))
            else:
                temp = int(str)
    elif line[0].isnumeric():
        # we're on a line with mappings
        mapping_str = line.split()
        mapping = []
        for str in mapping_str:
            mapping.append(int(str))
        mappings.append(mapping)
    if (len(line) == 1 and index != 1) or index == last:
        # we've hit the end of a section
        sources = []
        for mapping in mappings:
            # append tuple describing mapping as (start, end, offset),
            # where start and end are inclusive
            sources.append((mapping[1], mapping[1]+mapping[2]-1, mapping[0]-mapping[1]))
        seeds = sorted(seeds)
        sources = sorted(sources)
        max_i = len(sources)

        for seed_range in seeds:
            # list relevant sources
            relevant = []
            for source in sources:
                if (seed_range[0] <= source[0] <= seed_range[1]) or (seed_range[0] <= source[1] <= seed_range[1]) or (source[0] < seed_range[0] and source[1] > seed_range[1]):
                    relevant.append(source)
            
            for i, source in enumerate(relevant):
                if i == 0:
                    if source[0] > seed_range[0]:
                        # not in any source range, map unchanged
                        dests.append((seed_range[0], source[0]-1))
                    else:
                        # constrain start of source range to seed range
                        source = (seed_range[0], source[1], source[2])

                if source[1] > seed_range[1]:
                    # constrain end of source range to seed range
                    source = (source[0], seed_range[1], source[2])

                # append mapped tuple to dests
                dests.append((source[0]+source[2], source[1]+source[2]))

                if source[1] < seed_range[1]:
                    if i == len(relevant)-1:
                        # this was the last relevant source range, map remainder unchanged
                        dests.append((source[1]+1, seed_range[1]))
                    elif relevant[i+1][0] > source[1]+1:
                        # there's a gap between the end of this source range and the start
                        # of the next source range, map remainder unchanged
                        dests.append((source[1]+1, relevant[i+1][0]-1))

            if len(relevant) == 0:
                # no relevant mappings, map unchanged
                dests.append(seed_range)
        seeds = dests[:]
        dests = []
        mappings = []
# since we store our mappings as (start, end) inclusive tuples, the solution will always be the start of a tuple,
# so we can just find the lowest of these and take its 'start' value
print(min(seeds)[0])