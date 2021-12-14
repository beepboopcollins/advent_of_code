with open("input.txt") as file:
    puzzle_input = file.readlines()

import numpy as np
import matplotlib.pyplot as plt

ages = np.array([int(age) for age in puzzle_input[0].split(',')])
days = 150
reset_time = 6
mature_time = 2
population = []
initial_pop = len(ages)
for day in range(days):
    ages -= 1
    number_of_new_fish = np.sum(ages == -1)
    ages = np.where(ages == -1, reset_time, ages)
    ages = np.append(ages, np.full(number_of_new_fish,reset_time + mature_time))
    population.append(len(ages))
    print(day)

x = np.array(range(256 - days))
t = np.array(range(days, 256))
u = np.array(range(1,days+1))
y = population[-1]*2**(x/((reset_time+mature_time+reset_time+2)/2))
plt.plot(u, population)
plt.plot(t, y)
plt.yscale('log')
plt.show()

print(f"the answer to part two is {y[-1]}")
