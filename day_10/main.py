with open("input.txt") as file:
    puzzle_input = file.readlines()

lines = [line.replace("\n", "") for line in puzzle_input]

illegal_character_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
illegal_character_counts = {')': 0, ']': 0, '}': 0, '>': 0}
open_to_closed = {'(': ')', '[': ']', '{': '}', '<': '>'}
closed_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}
open_characters = '([{<'
incomplete_line_indices = list(range(len(lines)))

for i, line in enumerate(lines):
    expected_close_characters = []
    for char in line:
        if char in open_characters:
            expected_close_characters.append(open_to_closed[char])
        elif char == expected_close_characters[-1]:
            del expected_close_characters[-1]
        else:
            illegal_character_counts[char] += 1
            incomplete_line_indices.remove(i)
            break

syntax_score = sum(illegal_character_scores[char] * illegal_character_counts[char] for char in illegal_character_counts.keys())
print(f"the answer to part one is {syntax_score}")

incomplete_lines = [lines[i] for i in incomplete_line_indices]

completion_character_scores = {')':1,']':2,'}':3,'>':4}
completion_scores = []

for line in incomplete_lines:
    expected_close_characters = []
    for char in line:
        if char in open_characters:
            expected_close_characters.append(open_to_closed[char])
        elif char == expected_close_characters[-1]:
            del expected_close_characters[-1]
        else:
            raise Exception('oh no this line is busted')
    completion_string = ''.join(expected_close_characters[::-1])
    completion_score = 0
    for char in completion_string:
        completion_score *= 5
        completion_score += completion_character_scores[char]
    completion_scores.append(completion_score)

completion_scores.sort()
final_score = completion_scores[int(len(completion_scores)/2)]

print(f"the answer to part 2 is {final_score}")

