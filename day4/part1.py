class Solution():
    def part1(self, input_file='input.txt'):
        paperRollMap = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                paperRollMap.append(list(line.removesuffix('\n')))

        result = 0
        for x in range(len(paperRollMap)):
            for y in range(len(paperRollMap[x])):
                if (paperRollMap[x][y] == '@'):
                    adjacent = 0
                    for a in range(-1, 2):
                        for b in range(-1,2):
                            try:
                                if x==0 and y==0:
                                    adjacent += 0
                                elif paperRollMap[x-a][y-b] == "@":
                                    adjacent += 1
                            except IndexError:
                                adjacent += 0
                    
                    if(adjacent < 4):
                        result += 1

        return result


#.. 
#.@@
# 
# 


print(Solution().part1('input-test.txt'))