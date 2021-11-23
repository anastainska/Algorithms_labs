import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text_file = open("test_poker_in.txt", "r")
        test_poker_in_list = text_file.read().split(" ")
        test_poker_in_list = list(map(int, test_poker_in_list))
        poker = main.poker(test_poker_in_list)
        text_file.close()
        self.assertEqual(main.poker(test_poker_in_list), 7)


if __name__ == '__main__':
    unittest.main()
