import itertools

class Solution:
    def part1(self, input_file='input.txt'):
        joltageRatings = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                joltageRatings.append(line.removesuffix('\n'))

        returnSum = 0
        for rating in joltageRatings:

            possibleJoltages = set(itertools.combinations(rating, 2))
            returnSum += (int(''.join(sorted(list(possibleJoltages))[-1])))

        return returnSum
    
print(Solution().part1())