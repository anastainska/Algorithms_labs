import unittest
import main

comparisons = 0
execution_time = 0


class TestAlgo(unittest.TestCase):

    def test_merge_sort(self):
        main.order = 'asc'
        test_array = main.mergesort([1, 7, 3, 5, 2, -4, -5, 9, 23, 4, -6], main.order)
        test_answer = [-6,-5,-4,1,2,3,4,5,7,9,23]
        self.assertEqual(test_array, test_answer)

    def test_asc_sorted(self):
        main.order = 'asc'
        test_array = main.mergesort([1,2,3,4,5,6,7,8], main.order)
        test_answer = [1,2,3,4,5,6,7,8]
        self.assertEqual(test_array, test_answer)

    def test_desc(self):
        main.order = 'desc'
        test_array = main.mergesort([1,2,3,4,5,6,7,8], main.order)
        test_answer = [8,7,6,5,4,3,2,1]
        self.assertEqual(test_array, test_answer)

    def test_desc_sorted(self):
        main.order = 'desc'
        test_array = main.mergesort([8,7,6,5,4,3,2,1], main.order)
        test_answer = [8,7,6,5,4,3,2,1]
        self.assertEqual(test_array, test_answer)


if __name__ == '__main__':
    unittest.main()
