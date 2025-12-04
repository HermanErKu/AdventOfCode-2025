import unittest

import part1
import part2

class TestSolutions(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part1.Solution().part1('input-test.txt'), 13)

    # def test_part_2(self):
    #     self.assertEqual(part2.Solution().part2('input-test.txt'), 0)

if __name__ == '__main__':
    unittest.main()