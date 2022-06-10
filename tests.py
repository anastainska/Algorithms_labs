import unittest
from _operator import itemgetter

from graph import Graph

graph = {
    1: [[4, 5], [2, 6]],
    2: [[5, 3]],
    3: [[1, 1], [4, 5], [6, 4], [5, 6], [2, 5]],
    4: [[6, 2]]
}


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.g = Graph(6, graph)

    def test_prims_algorithm(self):
        self.assertEqual(sorted(self.g.prims_algorithm(), key=itemgetter(0, 1)),
                         sorted([[3, 2, 5], [2, 5, 3], [3, 1, 1], [3, 6, 4], [4, 6, 2]], key=itemgetter(0, 1)))


if __name__ == '__main__':
    unittest.main()