import unittest

from Heaps.TwoHeaps import MedianFinder


def medians_for(values):
    finder = MedianFinder()
    medians = []
    for value in values:
        finder.add(value)
        medians.append(finder.findMedian())
    return medians


class TestMedianFinder(unittest.TestCase):
    def test_single_value_is_the_median(self):
        self.assertEqual(medians_for([7]), [7])

    def test_even_count_uses_the_average_of_the_two_middle_values(self):
        self.assertEqual(medians_for([1, 2]), [1, 1.5])

    def test_odd_count_uses_the_middle_value(self):
        self.assertEqual(medians_for([1, 2, 3]), [1, 1.5, 2])

    def test_stream_can_arrive_unsorted(self):
        self.assertEqual(medians_for([3, 1, 2]), [3, 2.0, 2])

    def test_descending_stream(self):
        self.assertEqual(medians_for([5, 4, 3, 2, 1]), [5, 4.5, 4, 3.5, 3])

    def test_negative_numbers(self):
        self.assertEqual(medians_for([-1, -2, -3]), [-1, -1.5, -2])

    def test_duplicate_values(self):
        self.assertEqual(medians_for([2, 2, 2, 2]), [2, 2.0, 2, 2.0])

    def test_longer_mixed_stream(self):
        self.assertEqual(
            medians_for([8, 1, 6, 3, 4]),
            [8, 4.5, 6, 4.5, 4],
        )


if __name__ == "__main__":
    unittest.main()
