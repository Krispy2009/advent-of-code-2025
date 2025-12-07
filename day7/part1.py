beams = set()
splitters = set()
def process_beam(data):
    for idx, line in enumerate(data):
        if 'S' in line:
            start = (idx, line.index('S'))
            beams.add((start[0]+1, start[1]))
            continue
        for idx2, l in enumerate(line):
            if l == '.' and (idx-1,idx2) in beams:
                beams.add((idx, idx2))
                continue
            if l == '^' and (idx-1,idx2) in beams:
                if idx2-1 >= 0:
                    beams.add((idx+1, idx2-1))
                if idx2+1 < len(line):
                    beams.add((idx+1, idx2+1))
            if l == '^':
                splitters.add((idx, idx2))

def count_splits(splitters, beams):
    splits = 0
    for splitter in splitters:
        if (splitter[0]-1, splitter[1]) in beams:
            splits +=1
    return splits

def print_manifold(data):
    for idx, line in enumerate(data):
        for idx2, l in enumerate(line):
            if (idx, idx2) in beams:
                print("|", end="")
            else:
                print(l, end="")
        print()

data = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        data.append(list(line.strip()))

process_beam(data)
# print("splitters: ", splitters)


# print_manifold(data)
print("splits: ", count_splits(splitters, beams))