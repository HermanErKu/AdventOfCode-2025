class Solution:
    def part2(self, input_file='input.txt'):

        instructions = []

        with open(input_file,'r') as file:
            for line in file.readlines():
                instructions.append(line.removesuffix("\n"))

        dialValue = 50
        password = 0

        for instruction in instructions:
            newDialValue = dialValue

            direction = str(instruction)[:1]
            if direction == "R":
                newDialValue += int(str(instruction)[1:])
                while newDialValue >= 100:
                    newDialValue = newDialValue - 100
                    # if dialValue != 0 and newDialValue !=0: 
                    password += 1

            else:
                newDialValue -= int(str(instruction)[1:])
                while newDialValue < 0:
                    newDialValue = 100 + newDialValue
                    # if dialValue != 0 and newDialValue !=0: 
                    password += 1

            dialValue = newDialValue

            if dialValue == 0:
                password += 1

        # print(dialValue)
        # print(password)

        return password

print(Solution().part2())

#6671 too low
#7114 too high