import itertools

joltageRatings = []

with open('input2.txt', 'r') as file:
    for line in file.readlines():
        joltageRatings.append(line.removesuffix('\n'))

returnSum = 0
for rating in joltageRatings:

    possibleJoltages = set(itertools.combinations(rating, 2))
    returnSum += (int(''.join(sorted(list(possibleJoltages))[-1])))

print(returnSum)