with open("input.txt") as file:
    puzzle_input = file.read().split("\n")


def to_decimal(bits):
    powers_of_two = [2 ** e for e in range(len(gamma_rate))]
    powers_of_two.reverse()
    ans = 0
    for power_of_two, bit in zip(powers_of_two, bits):
        ans += bit * power_of_two
    return ans


# part one

transformed_input = [[int(char)] for char in puzzle_input[0]]
unique_vals = [0,1]

for line in puzzle_input[1:]:
    for n, char in enumerate(line):
        transformed_input[n].append(int(char))

gamma_rate = []
epsilon_rate = []

for pos in transformed_input:
    quantity_dict = {val: sum([x == val for x in pos]) for val in unique_vals}
    gamma_rate.append(max(quantity_dict, key=quantity_dict.get))
    epsilon_rate.append(min(quantity_dict, key=quantity_dict.get))

epsilon_rate_decimal = to_decimal(gamma_rate)
gamma_rate_decimal = to_decimal(epsilon_rate)


print(f"the answer to part one = {gamma_rate_decimal * epsilon_rate_decimal}")

# part two

# ox rating

transformed_input = [[int(char) for char in line] for line in puzzle_input]
possible_o2s = possible_co2s = transformed_input

n = 0
while len(possible_o2s) > 1 and n < len(possible_o2s[0]):
    pos = [possible_o2[n] for possible_o2 in possible_o2s]
    quantity_dict = {val: sum([x == val for x in pos]) for val in unique_vals}
    most_occurring = max(quantity_dict, key=quantity_dict.get)
    least_occurring = min(quantity_dict, key=quantity_dict.get)
    if most_occurring == least_occurring:
        most_occurring = 1
    possible_o2s = [possible_o2 for possible_o2 in possible_o2s if possible_o2[n] == most_occurring]
    n += 1
o2_rate = possible_o2s[0]

n = 0
while len(possible_co2s) > 1 and n < len(possible_co2s[0]):
    pos = [possible_co2[n] for possible_co2 in possible_co2s]
    quantity_dict = {val: sum([x == val for x in pos]) for val in unique_vals}
    most_occurring = max(quantity_dict, key=quantity_dict.get)
    least_occurring = min(quantity_dict, key=quantity_dict.get)
    if most_occurring == least_occurring:
        least_occurring = 0
    possible_co2s = [possible_co2 for possible_co2 in possible_co2s if possible_co2[n] == least_occurring]
    n += 1
co2_rate = possible_co2s[0]

o2_rate_decimal = to_decimal(o2_rate)
co2_rate_decimal = to_decimal(co2_rate)

print(f"the answer to part two is {o2_rate_decimal*co2_rate_decimal}")
pass
