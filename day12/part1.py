with open('input.txt', 'r') as file:
    lines = file.readlines()

gifts = {}
areas = []

for line in lines:
    if 'x' in line and line != '':
        areas.append(line.strip())
for idx in range(0, len(lines), 4):
    gift_area = ''.join(lines[idx+1:idx+4]).count('#')
    gifts[lines[idx][0]] = (lines[idx+1:idx+4], gift_area)



print(gifts)
print(areas)

total_enough_areas = 0

for area in areas:
    area, gifts_needed = area.split(':')
    area = [int(a) for a in area.split('x') if a != '']
    area = area[0] * area[1]
    print("This tree has an area of: ", area)
    gifts_needed = [int(g) for g in gifts_needed.split(' ') if g != '']
    print(gifts_needed)
    total_gifts_needed = sum(gifts_needed)
    print(total_gifts_needed)
    #check how many gifts can fit in the area including gaps
    print("9 * total_gifts_needed: ", 9 * total_gifts_needed)

    if 9 * total_gifts_needed <= area:
        print("This tree has enough area for the gifts")
        total_enough_areas += 1

print("total enough areas: ", total_enough_areas)