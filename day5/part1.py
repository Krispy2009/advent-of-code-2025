with open("input.txt", "r") as file:
    lines = file.readlines()
    fresh_ids = []
    ids_to_check = []
    for line in lines:
        if '-' in line:
            start, end = line.strip().split("-")
            fresh_ids.append((int(start), int(end)))
        else:
            if line.strip() != "":
                ids_to_check.append(int(line.strip()))

    fresh_ids.sort(key=lambda x: x[0])

    fresh_ids_list = []
    for id in ids_to_check:
        for fresh_id in fresh_ids:
            if id >= fresh_id[0] and id <= fresh_id[1]:
                fresh_ids_list.append(id)
                break
            elif id < fresh_id[0]:
                break
            else:
               continue

    print(len(fresh_ids_list))