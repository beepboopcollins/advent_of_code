with open("input.txt") as file:
    puzzle_input = file.readlines()

ages = [int(age) for age in puzzle_input[0].split(',')]

population = [0]*9

for age in ages:
    population[age] += 1

days = 256

for day in range(1,days+1):
    new = population.pop(0)
    population.append(0)
    population[6] += new
    population[8] += new
    print(day)

print(f"the answer is {sum(population)}")