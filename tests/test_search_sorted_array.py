from unittest import TestCase


class TestSearch_sorted_array(TestCase):
    def test_search_sorted_array(self):
        try:
            from build import search_sorted_array
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, search_sorted_array, None)
        self.assertEqual(search_sorted_array([3, 1, 2], 0), None)
        self.assertEqual(search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14, 1, 3, 5, 6, 7, 8, 9]
        self.assertEqual(search_sorted_array(data, val=1), 3)
        data = [1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(search_sorted_array(data, val=2), 2)
