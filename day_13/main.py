class Fold:
    def __init__(self, direction, magnitude):
        self.direction = direction
        self.magnitude = magnitude


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_x(self, r):
        self.x = 2 * r - self.x
        return self

    def reflect_y(self, r):
        self.y = 2 * r - self.y
        return self

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Grid:
    def __init__(self, dots_=None):
        if dots_ is None:
            dots_ = []
        if type(dots_) is not list:
            dots_ = [dots_]
        self.dots = set(dots_)
        self.shape = [max(self.dots, key=lambda d: d.x).x + 1, max(self.dots, key=lambda d: d.y).y + 1]

    def apply_fold(self, fold_):
        match fold_.direction:
            case "y":
                upper_dots = {dot_ for dot_ in self.dots if dot_.y < fold_.magnitude}
                lower_dots = {dot_ for dot_ in self.dots if dot_.y > fold_.magnitude}
                lower_dots_reflected = {dot_.reflect_y(fold_.magnitude) for dot_ in lower_dots}
                self.dots = upper_dots.union(lower_dots_reflected)

            case "x":
                left_dots = {dot_ for dot_ in self.dots if dot_.x < fold_.magnitude}
                right_dots = {dot_ for dot_ in self.dots if dot_.x > fold_.magnitude}
                right_dots_reflected = {dot_.reflect_x(fold_.magnitude) for dot_ in right_dots}
                self.dots = left_dots.union(right_dots_reflected)
            case _:
                raise Exception("wrong direction")

    def show(self):
        self.shape = [max(self.dots, key=lambda d: d.x).x + 1, max(self.dots, key=lambda d: d.y).y + 1]
        display_list = [['.'] * self.shape[0] for _ in range(self.shape[1])]
        for dot_ in self.dots:
            display_list[dot_.y][dot_.x] = '#'
        display_string = '\n'.join([' '.join(row) for row in display_list])
        print(display_string)


with open("input.txt") as file:
    puzzle_input = file.readlines()

dots = []
for line in puzzle_input[:puzzle_input.index('\n')]:
    coord = [int(x) for x in line.replace('\n', '').split(',')]
    dot = Dot(coord[0], coord[1])
    dots.append(dot)

grid = Grid(dots)
folds = []

for line in puzzle_input[puzzle_input.index('\n') + 1:]:
    parsed_fold = line.split('=')
    folds.append(Fold(parsed_fold[0][-1], int(parsed_fold[1])))

for fold in folds:
    grid.apply_fold(fold)

grid.show()
