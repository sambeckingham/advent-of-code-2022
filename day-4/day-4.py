input = open("./input", "r")
lines = input.readlines()

subset_total = 0
overlap_total = 0

for line in lines:
    ranges = line.strip().split(",")

    def parse_range(range_str):
        range_str = range_str.split("-")
        return set(range(int(range_str[0]), int(range_str[1]) + 1))

    first_range = parse_range(ranges[0])
    second_range = parse_range(ranges[1])

    if first_range <= second_range or second_range <= first_range:
        subset_total += 1

    if first_range & second_range:
        overlap_total += 1

print("Part 1: %d" % subset_total)
print("Part 2: %d" % overlap_total)
