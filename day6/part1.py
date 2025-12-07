import math

class Solution:
    def part1(self, input_file='input.txt'):
        data =[]
        with open(input_file, 'r') as file:
            for line in file.readlines():
                data.append(line)

        operationsDict = {}

        i = 0
        for line in data:
            numsArray = str(line).removesuffix('\n').split(' ')
            operations = []
            for num in numsArray:
                if num != '':

                    operations.append(num)

            operationsDict[i] = operations
            i += 1

        returnSum = 0
        for n in range(len(operationsDict[0])):
            evalString = ""
            for x in range(len(operationsDict)-1):
                evalString += str(operationsDict[x][n])
                evalString += str(operationsDict[len(operationsDict)-1][n])
            returnSum += eval(evalString[:-1])



        return returnSum




print(Solution().part1('input.txt'))