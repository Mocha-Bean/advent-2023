infile = open("day 6/input.txt", 'r', encoding="utf8")

line = infile.readline()
# remove everything before the colon
line = line.split(':')[1]
time_str = line.split()
time = []
for str in time_str:
    time.append(int(str))

line = infile.readline()
line = line.split(':')[1]
record_distance_str = line.split()
record_distance = []
for str in record_distance_str:
    record_distance.append(int(str))
sum = 0

for i, time in enumerate(time):
    # 'time' is the allotted time for race 'i'
    # no point in checking '0' or 'time' buttonpress
    ways_to_win = 0
    for press_duration in range(1, time):
        travel_time = time - press_duration
        distance = travel_time * press_duration
        if distance > record_distance[i]:
            ways_to_win += 1
    if sum == 0:
        sum = ways_to_win
    else:
        sum = sum * ways_to_win

print(sum)