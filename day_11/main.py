import numpy as np

with open("input.txt") as file:
    puzzle_input = file.readlines()

grid_size = len(puzzle_input)

cols = []

for line in puzzle_input:
    line = line.replace('\n', '')
    row = [int(char) for char in line]
    cols.append(row)


class Octopuses:
    def __init__(self, levels):
        self.energy_levels = np.array(levels)
        self.flashes = 0
        self.__already_flashed = self.__flash_now = np.full_like(self.energy_levels, False, dtype=bool)
        self.shape = self.energy_levels.shape
        self.size = np.prod(self.shape)

    def step(self):
        self.energy_levels += 1
        self.__already_flashed = np.full_like(self.energy_levels, False, dtype=bool)
        self.__flash_now = self.energy_levels > 9
        if self.__flash_now.any():
            self.__flash()
        flashes_this_step = np.sum(self.__already_flashed)
        self.flashes += flashes_this_step
        self.energy_levels = np.where(self.energy_levels > 9, 0, self.energy_levels)
        return flashes_this_step

    def __flash(self):
        ys, xs = np.where(self.__flash_now)
        for x, y in zip(xs, ys):
            add_mask = np.array([[max(abs(a-x),abs(b-y)) <= 1 for a in range(self.shape[0])] for b in range(self.shape[1])])
            self.energy_levels += add_mask
        self.__already_flashed = np.logical_or(self.__already_flashed, self.__flash_now)
        self.__flash_now = np.logical_and(self.energy_levels > 9, np.logical_not(self.__already_flashed))
        if self.__flash_now.any():
            self.__flash()


octos = Octopuses(cols)

number_of_steps = 100
steps = range(number_of_steps)

for step in steps:
    octos.step()

print(f"the answer to part one is {octos.flashes}")

octos = Octopuses(cols)
synced = False
step = 0

while not synced:
    flashes = octos.step()
    if flashes == octos.size:
        synced = True
    step += 1

print(f"the answer to part two is {step}")
