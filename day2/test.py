import unittest

import part1
import part2

result = part1.Solution().part1('input-test.txt')

part1.Solution().part1

class TestSolutions(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part1.Solution().part1('input-test.txt'), 1227775554)

    def test_part_2(self):
        self.assertEqual(part2.Solution().part2('input-test.txt'), 4174379265)

if __name__ == '__main__':
    unittest.main()