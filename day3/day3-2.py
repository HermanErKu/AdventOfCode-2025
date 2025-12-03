import functools

joltageRatings = []

with open('input2.txt', 'r') as file:
    for line in file.readlines():
        joltageRatings.append(line.removesuffix('\n'))

print(joltageRatings)

def monotonic_stack(array, k):
    n = len(array)
    remove = n-k
    stack = []
    for digit in array:
        while remove and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)
    return stack[:k]

returnSum = 0
for rating in joltageRatings:
    returnSum += int("".join(monotonic_stack(rating, 12)))

print(returnSum)