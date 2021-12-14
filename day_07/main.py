with open("input.txt") as file:
    puzzle_input = file.read()

crabs = [int(x) for x in puzzle_input.split(',')]

x = round(sum(crabs)/len(crabs))

def fuel_used(x, crabs):
    return sum([abs(x - crab) for crab in crabs])

carry_on = True

while carry_on:
    y = fuel_used(x, crabs)
    y_plus = fuel_used(x+1, crabs)
    y_minus = fuel_used(x-1, crabs)
    if y_plus < y:
        x = x + 1
    elif y_minus < y:
        x = x - 1
    else:
        carry_on = False

print(f"part one is {fuel_used(x,crabs)}")

def fuel_used2(x, crabs):
    distances = [abs(x - crab) for crab in crabs]
    return int(sum([distance*(distance+1)/2 for distance in distances]))
carry_on = True
while carry_on:
    y = fuel_used2(x, crabs)
    y_plus = fuel_used2(x+1, crabs)
    y_minus = fuel_used2(x-1, crabs)
    if y_plus < y:
        x = x + 1
    elif y_minus < y:
        x = x - 1
    else:
        carry_on = False

print(f"part two is {fuel_used2(x,crabs)}")