import unittest

import part1
import part2

result = part1.Solution().part1('input-test.txt')

part1.Solution().part1

class TestSolutions(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part1.Solution().part1('input-test.txt'), 3)

    def test_part_2(self):
        self.assertEqual(part1.Solution().part1('input-test.txt'), 6)

if __name__ == '__main__':
    unittest.main()