with open("input.txt", "r") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        max_num = 0
        for idx, ch in enumerate(line.strip()):
            for idx2, ch2 in enumerate(line.strip()):
                if idx2 <= idx:
                    continue
                
                num = int(str(ch) + str(ch2))
                if num > max_num:
                    max_num = num
        total += max_num

print("total: ", total)

