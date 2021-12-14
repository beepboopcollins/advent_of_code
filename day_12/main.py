import copy
with open("input.txt") as file:
    puzzle_input = file.readlines()

edges = [(line.split('-')[0].replace('\n', ''), line.split('-')[1].replace('\n', '')) for line in puzzle_input]
nodes = set()
cave_system = {}
for edge in edges:
    for node in edge:
        nodes.add(node)
    if edge[0] in cave_system:
        cave_system[edge[0]].append(edge[1])
    else:
        cave_system[edge[0]] = [edge[1]]
    if edge[1] in cave_system:
        cave_system[edge[1]].append(edge[0])
    else:
        cave_system[edge[1]] = [edge[0]]

big_caves = {node for node in nodes if node.isupper()}
small_caves = nodes.difference(big_caves)
small_caves.remove("end")
small_caves.remove("start")

paths = []


def next_step_part_one(path, next_node, already_visited):
    path.append(next_node)
    if next_node == 'end':
        paths.append(path)
        return
    already_visited.add(next_node)
    possible_nodes = cave_system[next_node]
    for possible_node in possible_nodes:
        if possible_node in small_caves:
            if possible_node not in already_visited:
                next_step_part_one(path.copy(), possible_node, already_visited.copy())
            else:
                continue
        elif possible_node in big_caves:
            next_step_part_one(path.copy(), possible_node, already_visited.copy())
        elif possible_node == "end":
            next_step_part_one(path.copy(), possible_node, already_visited.copy())
        elif possible_node == "start":
            continue
        else:
            raise Exception("something wrong")


next_step_part_one([], 'start', set())

print(f"the answer to aprt one is {len(paths)}")


def next_step_part_two(path, next_node, already_visited, double_visited_small_cave):
    path.append(next_node)
    if next_node == 'end':
        paths.append(path)
        return
    already_visited.add(next_node)
    possible_nodes = cave_system[next_node]

    for possible_node in possible_nodes:
        if possible_node in small_caves:
            if possible_node not in already_visited:
                next_step_part_two(path.copy(), possible_node, already_visited.copy(), double_visited_small_cave)
            elif not double_visited_small_cave:
                next_step_part_two(path.copy(), possible_node, already_visited.copy(), True)
            else:
                continue
        elif possible_node in big_caves:
            next_step_part_two(path.copy(), possible_node, already_visited.copy(), double_visited_small_cave)
        elif possible_node == "end":
            next_step_part_two(path.copy(), possible_node, already_visited.copy(), double_visited_small_cave)
        elif possible_node == "start":
            continue
        else:
            raise Exception("uh ohhhh")


paths = []
next_step_part_two([], 'start', set(), False)

print(f"the answer to aprt one is {len(paths)}")

