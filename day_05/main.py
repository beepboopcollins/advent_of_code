import numpy as np


class OceanFloor:
    def __init__(self, shape):
        self.shape = shape
        self.map = np.zeros(shape, dtype=int)

    def add_vent(self, vent):
        if vent.start[0] == vent.end[0]:
            self.__add_horizontal_vent(vent)
        elif vent.start[1] == vent.end[1]:
            self.__add_vertical_vent(vent)
        elif abs((vent.start[1] - vent.end[1])/(vent.start[0] - vent.end[0])) == 1:
            self.__add_diagonal_vent(vent)
        else:
            Exception("this vent is too weird :S")

    def count_dangerous_points(self):
        return np.sum(self.map > 1)

    def __add_horizontal_vent(self, vent):
        small_y = min(vent.start[1], vent.end[1])
        big_y = max(vent.start[1], vent.end[1])
        coords = [[vent.start[0], y] for y in range(small_y, big_y + 1)]
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.map[x, y] += 1

    def __add_vertical_vent(self, vent):
        small_x = min(vent.start[0], vent.end[0])
        big_x = max(vent.start[0], vent.end[0])
        coords = [[x, vent.start[1]] for x in range(small_x, big_x + 1)]
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.map[x, y] += 1

    def __add_diagonal_vent(self, vent):
        if vent.start[0] > vent.end[0]:
            x_increment = -1
        else:
            x_increment = 1
        if vent.start[1] > vent.end[1]:
            y_increment = -1
        else:
            y_increment = 1
        coords = [[x, y] for x, y in zip(range(vent.start[0], vent.end[0] + x_increment, x_increment), range(vent.start[1], vent.end[1] + y_increment, y_increment))]
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.map[x, y] += 1


class Vent:
    def __init__(self, start, end):
        self.start = tuple(start)
        self.end = tuple(end)


with open("input.txt") as file:
    puzzle_input = file.readlines()

shape = (1000, 1000)
ocean_floor = OceanFloor(shape)
vents = []

for line in puzzle_input:
    split_line = line.split(' -> ')
    coords = []
    for item in split_line:
        coords.append([int(x) for x in item.split(',')])
    vents.append(Vent(coords[0], coords[1]))

for vent in vents:
    ocean_floor.add_vent(vent)

print(f"the answer to part two is {ocean_floor.count_dangerous_points()}")

