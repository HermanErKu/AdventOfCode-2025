class Solution():
    def monotonic_stack(self, array, k):
        n = len(array)
        remove = n-k
        stack = []
        for digit in array:
            while remove and stack and stack[-1] < digit:
                stack.pop()
                remove -= 1
            stack.append(digit)
        return stack[:k]
    
    def part2(self, input_file='input.txt'):
        joltageRatings = []

        with open(input_file, 'r') as file:
            for line in file.readlines():
                joltageRatings.append(line.removesuffix('\n'))


        returnSum = 0
        for rating in joltageRatings:
            returnSum += int("".join(Solution().monotonic_stack(rating, 12)))

        return returnSum

print(Solution().part2())