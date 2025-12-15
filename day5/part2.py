class Solution:
    def part2(self, input_file='input.txt'):
        freshIngredientRanges = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                if '-' in line:
                    freshIngredientRanges.append(line.removesuffix('\n'))

        freshIngredientRanges.sort(key=lambda item: int(str(item).split('-')[0]))
        print(freshIngredientRanges)

        freshIngredients = 0
        listIndex = 0
        pointer1 = int(str(freshIngredientRanges[listIndex]).split('-')[0])
        pointer2 = int(str(freshIngredientRanges[listIndex]).split('-')[1])

        while listIndex < len(freshIngredientRanges)-1:
            listIndex += 1
            if int(str(freshIngredientRanges[listIndex]).split('-')[0]) < pointer2:
                pointer2 = int(str(freshIngredientRanges[listIndex]).split('-')[0])
            else:
                pointer1 = int(str(freshIngredientRanges[listIndex]).split('-')[0])
                pointer2 = int(str(freshIngredientRanges[listIndex]).split('-')[1])
            
            print(pointer1, pointer2)
        
            diff = abs(pointer1-pointer2)
            freshIngredients+= diff

        # for i in range(len(freshIngredientRanges)):
        #     num1 = int(str(freshIngredientRanges[i]).split('-')[0])
        #     num2 = int(str(freshIngredientRanges[i]).split('-')[1])

        #     pointer1 = num1
        #     pointer2 = num2

        #     while int(str(freshIngredientRanges[i+1]).split('-')[0]) < int(str(freshIngredientRanges[i]).split('-')[1]):
        #         pointer2 = int(str(freshIngredientRanges[i+1]).split('-')[1])
        #         i += 1
        #         break
        #     print(pointer1, pointer2)

        #     diff = abs(pointer1-pointer2)

        #     freshIngredients += diff


        return freshIngredients
    

# sort freshIngredientRanges on first index
# diff = 0
# 2 pointers
# pointer 1 = freshIngredientRange[n][0]
# while freshIngredientRange[n+1][0] < freshIngredientRange[n][1]: pointer2 = freshIngredientRange[n+1][1]
# diff += abs(pointer2,pointer1)
    
print(Solution().part2('input-test.txt'))