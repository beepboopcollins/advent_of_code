import numpy as np


class BingoGrid:
    def __init__(self, size):
        self.size = size
        self.nums = np.full((size, size), -1, dtype=int)
        self.checked = np.full((size, size), False, dtype=bool)
        self.__won = False

    def check_num(self, val):
        coords = np.where(self.nums == val)
        if coords:
            xs,ys = coords
            for x, y in zip(xs,ys):
                self.checked[x, y] = True
            return True
        else:
            return False

    def has_won(self):
        if self.__won:
            return True
        if self.__is_a_row_checked() or self.__is_a_col_checked():
            self.__won = True
            return True
        else:
            return False

    def __is_a_row_checked(self):
        for y in range(self.size):
            row = self.checked[:, y]
            if all(row):
                return True
        return False

    def __is_a_col_checked(self):
        for x in range(self.size):
            col = self.checked[x, :]
            if all(col):
                return True
        return False

    def calc_score(self, last_called_num):
        if not self.__won:
            if not self.has_won():
                return False
            else:
                self.__won = True
        score = np.sum(self.nums * np.logical_not(self.checked))*last_called_num
        return score

    def is_full(self):
        return -1 not in self.nums


with open("input.txt") as file:
    puzzle_input = file.readlines()

bingo_numbers = [int(num) for num in puzzle_input[0].replace('\n', '').split(',')]
grid_size = 5
grids = []
y = 0
for line in puzzle_input[1:]:
    line = line.replace('\n', '')
    if not line:
        y = 0
        grids.append(BingoGrid(grid_size))
    else:
        row = [int(x) for x in line.split(' ') if x]
        grids[-1].nums[:, y] = row
        y += 1

game_over = False
for drawn_number in bingo_numbers:
    for grid in grids:
        grid.check_num(drawn_number)
        if grid.has_won():
            winning_grid = grid
            score = grid.calc_score(drawn_number)
            game_over = True
            break
    if game_over:
        break

print(f"the answer to part one is {score}")

# part two
grids = []
y = 0
for line in puzzle_input[1:]:
    line = line.replace('\n', '')
    if not line:
        y = 0
        grids.append(BingoGrid(grid_size))
    else:
        row = [int(x) for x in line.split(' ') if x]
        grids[-1].nums[:, y] = row
        y += 1

game_over = False
for drawn_number in bingo_numbers:
    for grid in grids:
        grid.check_num(drawn_number)
    grids = [grid for grid in grids if not grid.has_won()]
    if len(grids) == 1:
        last_grid = grids[0]
    elif len(grids) == 0:
        score = last_grid.calc_score(drawn_number)
        break
print(f"the answer to part two is {score}")
