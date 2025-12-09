import math
from collections import defaultdict
distances = {}
points = []
circuits = defaultdict(list)
import uuid
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit_id = str(uuid.uuid4())
        circuits[self.circuit_id].append(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def add_to_circuit(self, point):
        circuits[self.circuit_id] = []
        self.circuit_id = point.circuit_id
        circuits[point.circuit_id].append(self)
        # del circuits[self.circuit_id]
        
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

def calc_eucledian_distance(point1, point2):
    if point1.circuit_id == point2.circuit_id:
        return 0
    return (point1.x-point2.x)**2 + (point1.y-point2.y)**2 + (point1.z-point2.z)**2

def join_circuits(point1: Point, point2: Point):
    if point1.circuit_id != point2.circuit_id:
        for p in circuits[point2.circuit_id]:
            p.add_to_circuit(point1)

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        x, y, z = map(int, line.split(","))
        p = Point(x, y, z)
        # print(p)
        points.append(p)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances[points[i], points[j]] = calc_eucledian_distance(points[i], points[j])

sorted_distances = sorted(distances.items(), key=lambda x: x[1])


ITERATIONS = 1000

while ITERATIONS > 0:
    # import pdb; pdb.set_trace()
    dist = sorted_distances[0]
    point1, point2 = dist[0]
    join_circuits(point1, point2)
    sorted_distances.remove(dist)
    ITERATIONS -= 1

circuit_details = sorted([len(v) for v in circuits.values() if len(v) > 0], reverse=True)

# print(circuit_details)
print("there are ", len(circuit_details), " circuits")
# print(circuits)
print("Multipling top 3 circuits: ", circuit_details[0] * circuit_details[1] * circuit_details[2])