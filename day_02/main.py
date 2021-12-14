with open("input.txt") as file:
    puzzle_input = file.read().split("\n")

# part one

depth = 0
horizontal_position = 0

for instruction in puzzle_input:
    direction, magnitude = instruction.split(" ")
    magnitude = int(magnitude)
    match direction:
        case "up":
            depth -= magnitude
        case "down":
            depth += magnitude
        case "forward":
            horizontal_position += magnitude
        case _:
            Exception("oops wrong direction")

print(f"part one answer = {depth*horizontal_position}")

#part 2

aim = 0
horizontal_position = 0
depth = 0

for instruction in puzzle_input:
    direction, magnitude = instruction.split(" ")
    magnitude = int(magnitude)
    match direction:
        case "up":
            aim -= magnitude
        case "down":
            aim += magnitude
        case "forward":
            horizontal_position += magnitude
            depth += aim*magnitude
        case _:
            Exception("oops wrong direction")

print(f"part two answer = {depth*horizontal_position}")

