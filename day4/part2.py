class Solution():
    def part2(self, input_file='input.txt'):
        paperRollMap = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                paperRollMap.append(list(line.removesuffix('\n')))

        result = 0
        for row in range(len(paperRollMap)):
            for col in range(len(paperRollMap[row])):
                if (paperRollMap[row][col] == "@"):
                    adjacent = 0
                    for rowSearch in range(-1,2):
                        for colSearch in range(-1,2):
                            if (rowSearch == 0 and colSearch == 0):
                                continue
                            
                            newRow = row + rowSearch
                            newCol = col + colSearch
                            
                            if (newRow < 0 or newCol < 0):
                                continue
                            if (newRow >= len(paperRollMap) or newCol >= len(paperRollMap[newRow])):
                                continue
                            
                            if (paperRollMap[newRow][newCol] == "@"):
                                adjacent += 1

                    if adjacent < 4:
                        result += 1

        return result



print(Solution().part2('input.txt'))