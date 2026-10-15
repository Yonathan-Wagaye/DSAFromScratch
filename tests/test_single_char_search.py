import unittest

from Backtracking.singleCharSearch import (
    singleCharSearchGraphDFS,
    singleCharSearchLoopVariation,
    singleCharSearchRecursiveVariant,
)


class CharacterSearchContract:
    """Expected behavior for every single-character search implementation."""

    def test_returns_false_for_empty_grid(self):
        self.assertFalse(self.search([], "A"))
        self.assertFalse(self.search([[]], "A"))

    def test_finds_target_in_single_cell_grid(self):
        self.assertTrue(self.search([["A"]], "A"))

    def test_rejects_missing_target_in_single_cell_grid(self):
        self.assertFalse(self.search([["A"]], "B"))

    def test_finds_target_at_every_corner_and_the_middle(self):
        grid = [
            ["A", "B", "C", "E"],
            ["S", "F", "G", "H"],
            ["I", "J", "K", "L"],
        ]
        cases = [
            ("A", "top-left"),
            ("E", "top-right"),
            ("F", "middle"),
            ("I", "bottom-left"),
            ("L", "bottom-right"),
        ]

        for target, position in cases:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.search(grid, target))

    def test_finds_example_character(self):
        grid = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

        self.assertTrue(self.search(grid, "D"))

    def test_returns_false_when_target_is_absent(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
        ]

        self.assertFalse(self.search(grid, "Z"))

    def test_searches_a_single_row(self):
        grid = [["A", "B", "C", "D"]]

        self.assertTrue(self.search(grid, "A"))
        self.assertTrue(self.search(grid, "D"))
        self.assertFalse(self.search(grid, "Z"))

    def test_searches_a_single_column(self):
        grid = [["A"], ["B"], ["C"], ["D"]]

        self.assertTrue(self.search(grid, "A"))
        self.assertTrue(self.search(grid, "D"))
        self.assertFalse(self.search(grid, "Z"))

    def test_finds_a_repeated_character(self):
        grid = [
            ["A", "X", "C"],
            ["D", "E", "X"],
        ]

        self.assertTrue(self.search(grid, "X"))

    def test_distinguishes_characters_that_differ_only_by_case(self):
        self.assertFalse(self.search([["a"]], "A"))
        self.assertTrue(self.search([["a"]], "a"))

    def test_does_not_modify_the_grid(self):
        grid = [
            ["A", "B"],
            ["C", "D"],
        ]
        original = [row.copy() for row in grid]

        self.search(grid, "D")
        self.search(grid, "Z")

        self.assertEqual(grid, original)


class TestSingleCharSearchGraphDFS(CharacterSearchContract, unittest.TestCase):
    search = staticmethod(singleCharSearchGraphDFS)


class TestSingleCharSearchLoopVariation(CharacterSearchContract, unittest.TestCase):
    search = staticmethod(singleCharSearchLoopVariation)


class TestSingleCharSearchRecursiveVariant(CharacterSearchContract, unittest.TestCase):
    search = staticmethod(singleCharSearchRecursiveVariant)


if __name__ == "__main__":
    unittest.main()
