class Solution:
    def part1(self, input_file='input.txt'):
        freshIngredientRanges = []
        availableIngredients = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                if '-' in line:
                    freshIngredientRanges.append(line.removesuffix('\n'))
                
                elif len(line) >1:
                    availableIngredients.append(line.removesuffix('\n'))

        freshIngredientRanges.sort(key=lambda item: int(str(item).split('-')[0]))
        availableFreshIngredients = 0

        for availableIngredient in availableIngredients:
            for freshIngredientRange in freshIngredientRanges:
                low, high = int(str(freshIngredientRange).split('-')[0]), int(str(freshIngredientRange).split('-')[1])
                if int(availableIngredient) >= low and int(availableIngredient) <= high:
                    availableFreshIngredients += 1
                    break

        return availableFreshIngredients
    
print(Solution().part1('input.txt'))