import unittest

from main import rabin_karp


class TestQuickSort(unittest.TestCase):
    def test_rabin_karp_1(self):
        pattern = "12kas"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1a" \
                "bc12sfabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12kas23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcab"

        self.assertEqual(rabin_karp(pattern, text1), 1)

    def test_rabin_karp_2(self):
        pattern = "abc"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1a" \
                "bc12sfabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12kas23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcab"

        self.assertEqual(rabin_karp(pattern, text1), 87)

    def test_rabin_karp_3(self):
        pattern = "12k23"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1a" \
                "bc12sfabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12kas23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
                "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
                "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
                "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcab"

        self.assertEqual(rabin_karp(pattern, text1), 10)