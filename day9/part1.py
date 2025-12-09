import math
from collections import defaultdict
points = []
distances = defaultdict(int)

def calc_eucledian_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        points.append(tuple(map(int, line.split(","))))

for point in points:
    for other_point in points:
        if point != other_point:
            distances[(point, other_point)] = calc_eucledian_distance(point, other_point)


# print(distances)

longest_distance_point = max(distances.items(), key=lambda x: x[1])
print("longest distance point: ", longest_distance_point)

def calculate_area(point1, point2):
    return (abs(point1[0] - point2[0])+1) * (abs(point1[1] - point2[1])+1)

print("area: ", calculate_area(longest_distance_point[0][0], longest_distance_point[0][1]))