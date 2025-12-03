class Solution():
    def part1(self, input_file='input.txt'):
        instructions = []

        with open(input_file,'r') as file:
            for line in file.readlines():
                instructions.append(line.removesuffix("\n"))

        dialValue = 50
        password = 0

        for instruction in instructions:
            if str(instruction).startswith("R"):
                dialValue += int(str(instruction)[1:])
                while dialValue >= 100:
                    dialValue = dialValue - 100
            else:
                dialValue -= int(str(instruction)[1:])
                while dialValue < 0:
                    dialValue = 100 + dialValue
            
            if dialValue == 0:
                password += 1

        return password

print(Solution().part1())