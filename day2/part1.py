import re

class Solution:
    def part1(self, input_file='input.txt'):
        ids = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                ids = line.split(',')
                    
        returnNumber = 0
        for pair in ids:
            num1 = int(pair.split("-")[0])
            num2 = int(pair.split("-")[1])

            if num1 > num2:
                num1, num2 = num2, num1

            rangeList = list(range(num1, num2 + 1))
            for num in rangeList:
                if re.fullmatch(r"(.+)\1", str(num)):
                    returnNumber += int(num)
                
        return returnNumber

print(Solution().part1())