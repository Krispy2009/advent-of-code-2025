fresh_id_ranges = []
checked_ranges = []
num_ids = 0

def are_there_overlapping_ranges(range, ranges):
    overlapping_ranges = []
    for r in ranges:
        if r == range:
            continue
        if is_overlapping(range, r):
            overlapping_ranges.append(r)
    return overlapping_ranges != []

def is_overlapping(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]

def merge_ranges(range1, range2):
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

def process_ranges(ranges):
    for i, r in enumerate(ranges):
        # print("Checking range:", r)
        if i < len(ranges) - 1 and is_overlapping(r, ranges[i+1]):
            # print("r:", r, "is_overlapping with:", ranges[i+1])
            new_range = merge_ranges(r, ranges[i+1])
            # print("new_range:          ", new_range)
            # print("ranges:             ", ranges)
            ranges.pop(i)
            # print("ranges after pop:   ", ranges)
            ranges[i] = new_range
            # print("ranges after update:", ranges)
        elif i > 0 and is_overlapping(r, ranges[i-1]):
            # print("r:", r, "is_overlapping with:", ranges[i-1])
            new_range = merge_ranges(r, ranges[i-1])
            # print("new_range:          ", new_range)
            # print("ranges:             ", ranges)
            ranges.pop(i)
            # print("ranges after pop:   ", ranges)
            ranges[i-1] = new_range
            # print("ranges after update:", ranges)
        else:
            continue
    return ranges

with open("input.txt", "r") as file:
    lines = file.readlines()
    unique_num_ids = 0
    ranges = []
    for line in lines:
        if '-' in line:
            start, end = line.strip().split("-")
            ranges.append((int(start), int(end)))
    ranges = sorted(ranges, key=lambda x: x[0])

    ranges = process_ranges(ranges)
    
    for r in ranges:
        if are_there_overlapping_ranges(r, ranges):
            ranges = process_ranges(ranges)
              
    print("sum:", sum([r[1] - r[0] + 1 for r in ranges]))
