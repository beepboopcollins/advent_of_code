with open("input.txt") as file:
    puzzle_input = file.readlines()

import numpy as np

height_map = np.array([[int(char) for char in line.replace('\n','')] for line in puzzle_input])

low_points = np.full_like(height_map, False)
width = height_map.shape[0]
length = height_map.shape[1]
for x in range(width):
    for y in range(length):
        up = down = left = right = False
        h = height_map[x, y]
        if x == 0 or height_map[x - 1, y] > h:
            left = True
        if x == width - 1 or height_map[x + 1, y] > h:
            right = True
        if y == 0 or height_map[x, y - 1] > h:
            down = True
        if y == length - 1 or height_map[x, y + 1] > h:
            up = True
        low_points[x, y] = up and down and left and right

risk = np.sum(1 + np.where(low_points, height_map,-1))

print(f"the answer to part one is {risk}")

basin_values = np.zeros_like(height_map)

for x in range(width):
    for y in range(length):
        if height_map[x, y] == 9:
            continue
        working_x = x
        working_y = y
        while not low_points[working_x, working_y]:
            up = down = left = right = False
            h = height_map[working_x, working_y]
            if working_x != 0 and height_map[working_x - 1, working_y] < h:
                working_x -= 1
            elif working_x != width - 1 and height_map[working_x + 1, working_y] < h:
                working_x += 1
            elif working_y != length - 1 and height_map[working_x, working_y + 1] < h:
                working_y += 1
            elif working_y != 0 and height_map[working_x, working_y - 1] < h:
                working_y -= 1
            else:
                raise Exception("hmmmm we should be in basin")
        basin_values[working_x, working_y] += 1

explode_basin_values = np.concatenate(basin_values)
explode_basin_values.sort()
basin_score = np.prod(explode_basin_values[-3:])

print(f"the answer to part two is {basin_score}")

