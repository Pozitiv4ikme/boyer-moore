import unittest

from boyer_moore import BoyerMoore


class TestBoyerMooreSearch(unittest.TestCase):
    def test_search_case1(self):
        text = "hi Peter"
        pattern = "hi"
        test = BoyerMoore(pattern, text)
        search_resul = test.search()

        self.assertEqual(search_resul, [0], "Should be 0")

    def test_search_case2(self):
        text = "hello hello"
        pattern = "hello"
        test = BoyerMoore(pattern, text)
        search_resul = test.search()

        self.assertEqual(search_resul, [0, 6], "Should be [0, 6]")

    def test_search_case3(self):
        text = "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
        pattern = "SSSS"
        test = BoyerMoore(pattern, text)
        search_resul = test.search()

        self.assertEqual(search_resul, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                        21, 22, 23, 24, 25, 26, 27],
                         "Should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "
                         "21, 22, 23, 24, 25, 26, 27]")
