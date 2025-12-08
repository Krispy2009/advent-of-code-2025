from collections import defaultdict
beams = defaultdict(int)
splitters = set()
def process_beam(data):
    for idx, line in enumerate(data):
        if 'S' in line:
            start = (idx, line.index('S'))
            beams[(start[0]+1, start[1])] += 1
            continue
        for idx2, l in enumerate(line):
            if l == '.' and (idx-1,idx2) in beams:
                beams[(idx+1, idx2)] += beams[(idx-1, idx2)]
                continue
            if l == '^' and (idx-1,idx2) in beams:
                if idx2-1 >= 0:
                    beams[(idx+1, idx2-1)] += beams[(idx-1, idx2)]
                if idx2+1 < len(line):
                    beams[(idx+1, idx2+1)] += beams[(idx-1, idx2)]

data = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        data.append(list(line.strip()))

process_beam(data)

sum =0
for beam in beams:
    if beam[0] == len(data)-1:
        sum += beams[beam]
print("sum: ", sum)
