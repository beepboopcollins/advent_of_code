with open("input.txt") as file:
    puzzle_input = file.read().split('\n')

# part 1

puzzle_input = [int(x) for x in puzzle_input]

number_of_increases = 0
number_of_decreases = 0
number_of_equal = 0

for prev_val, val in zip(puzzle_input[0:-1], puzzle_input[1:]):
    if val > prev_val:
        number_of_increases += 1
    elif val < prev_val:
        number_of_decreases += 1
    else:
        number_of_equal += 1

print(f'part one answer = {number_of_increases}')

# part 2

sliding_average = [sum(x)/len(x) for x in zip(puzzle_input, puzzle_input[1:], puzzle_input[2:])]

number_of_increases = 0
number_of_decreases = 0
number_of_equal = 0

for prev_val, val in zip(sliding_average[0:-1], sliding_average[1:]):
    if val > prev_val:
        number_of_increases += 1
    elif val < prev_val:
        number_of_decreases += 1
    else:
        number_of_equal += 1

print(f'part two answer = {number_of_increases}')