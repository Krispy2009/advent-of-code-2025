def count_papers(position, lines):
    # print(f"position: {position}")
    row, col = position
    num_papers = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0].strip()):
                continue
            # print(f"i: {i}, j: {j}, lines[i][j]: {lines[i][j]}")
            if lines[i][j] == "@" and (i, j) != position:
                num_papers += 1
    # print(f"num_papers: {num_papers}")
    return num_papers

def find_possible_spaces(lines):
    possible_spaces = []
    for idx1, row in enumerate(lines):
        for idx2, col in enumerate(row.strip()):
            if col == "@":
                num_papers = count_papers((idx1, idx2), lines)
                if num_papers < 4:
                    possible_spaces.append((idx1, idx2))
    return possible_spaces

def remove_papers(lines, possible_spaces):
    for space in possible_spaces:
        lines[space[0]] = list(lines[space[0]])
        lines[space[0]][space[1]] = "."
        lines[space[0]] = "".join(lines[space[0]])
    return lines

with open("input.txt", "r") as file:
    lines = file.readlines()
    possible_spaces = find_possible_spaces(lines)
    lines = remove_papers(lines, possible_spaces)
    removed_papers = len(possible_spaces)
    while len(possible_spaces) > 0:
        possible_spaces = find_possible_spaces(lines)
        lines = remove_papers(lines, possible_spaces)
        removed_papers += len(possible_spaces)
    print("removed_papers: ", removed_papers)

        