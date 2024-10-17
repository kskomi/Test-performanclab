import sys
import math

def point_position(circle_file, points_file):
    with open(circle_file, 'r') as f:
        cx, cy = map(float, f.readline().split())
        r = float(f.readline().strip())

    with open(points_file, 'r') as f:
        points = [list(map(float, line.split())) for line in f]

    for x, y in points:
        distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        if distance < r:
            print(1)
        elif distance == r:
            print(0)
        else:
            print(2)

if __name__ == "__main__":
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    point_position(circle_file, points_file)

