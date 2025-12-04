import itertools
from re import L

BANKS = 12


def find_max_num(line):    
    stack = []
    remaining = len(line) - BANKS
    # print("remaining: ", remaining)
    for ch in line:
        while remaining > 0 and len(stack) > 0 and stack[-1] < ch:

            stack.pop()
            remaining -= 1
        stack.append(ch)
        # print("stack: ", stack, "remaining: ", remaining)

    # print("stack: ", stack[:BANKS])
    max_num = int("".join(stack[:BANKS]))
    # print("max num: ",  max_num )
    return int((max_num))


with open("input.txt", "r") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total += find_max_num(line.strip())

print("total: ", total)
