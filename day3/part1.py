import itertools

def find_max_num(line):
    max_num = 0
    for combo in itertools.combinations(line.strip(), 2):
        num = int("".join(combo))
        if num > max_num:
            max_num = num
    # print(max_num)
    return max_num

with open("input.txt", "r") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total += find_max_num(line)

print("total: ", total)