joltageRatings = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        joltageRatings.append(line.removesuffix('\n'))

returnSum = 0
for rating in joltageRatings:
    possibleJoltages = set()

    for i in range(len(rating)):
        for x in range(i+1, len(rating)):
            possibleJoltages.add(int(rating[i]+rating[x]))
    
    returnSum += int(sorted(list(possibleJoltages))[-1])

print(returnSum)