import math
infile = open("day 6/input.txt", 'r', encoding="utf8")

line = infile.readline()
# remove everything before the colon
line = line.split(':')[1]
time_str = line.split()
actual_time_str = ""
for str in time_str:
    actual_time_str += str
time = int(actual_time_str)

line = infile.readline()
line = line.split(':')[1]
record_distance_str = line.split()
actual_record_distance_str = ""
for str in record_distance_str:
    actual_record_distance_str += str
record_distance = int(actual_record_distance_str)

t = float(time)
g = float(record_distance)

# quadratic formula (sing the jingle)
intercept_0 = (-t + math.sqrt((-t)*(-t) - 4*g))/-2
intercept_1 = (-t - math.sqrt((-t)*(-t) - 4*g))/-2

# lowest press duration that will get above record distance:
thresh_0 = math.ceil(intercept_0)
# highest press duration that will get above record distance:
thresh_1 = math.floor(intercept_1)

ways_to_win = thresh_1 - thresh_0 + 1

print(ways_to_win)