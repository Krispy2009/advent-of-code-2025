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

with open("input.txt", "r") as file:
    lines = file.readlines()
    possible_spaces = 0
    for idx1, row in enumerate(lines):
        for idx2, col in enumerate(row.strip()):
            if col == "@":
                num_papers = count_papers((idx1, idx2), lines)
                if num_papers < 4:
                    possible_spaces += 1

    print("possible_spaces: ", possible_spaces)

        