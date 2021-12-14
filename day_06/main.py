class LanternFish:
    reset_time = 6
    mature_time = 2

    def __init__(self, age=reset_time, is_juvenile=True):
        self.age = age
        self.is_juvenile = is_juvenile
        if self.is_juvenile:
            self.age += self.mature_time

    def simulate_day(self):
        self.age -= 1
        if self.age < 0:
            self.age = self.reset_time
            self.is_juvenile = False
            return True


class Population:

    def __init__(self, ages):
        self.population = []
        for age in ages:
            self.population.append(LanternFish(age=age, is_juvenile=False))
        self.ages = ages
        self.total_pop = len(self.population)

    def simulate_day(self):
        new_pop = []
        for fish in self.population:
            if fish.simulate_day():
                new_pop.append(LanternFish())
        self.population.extend(new_pop)
        self.total_pop = len(self.population)
        self.ages = [fish.age for fish in self.population]


with open("input.txt") as file:
    puzzle_input = file.readlines()

ages = [int(age) for age in puzzle_input[0].split(',')]

ocean_pop = Population(ages)

for day in range(256):
    print(f"day = {day}")
    ocean_pop.simulate_day()

print(f"the answer to part one is {ocean_pop.total_pop}")
