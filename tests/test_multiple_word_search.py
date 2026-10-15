import unittest

from Backtracking.multipleWordSearch import (
    naiveMutipleWordSearch,
    optimalMutipleWordSearch,
)

EXAMPLE_BOARD = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]

FACT_GRID = [
    ["T", "C", "O", "E"],
    ["E", "A", "F", "C"],
    ["L", "T", "S", "A"],
]

SNAKE_GRID = [
    ["A", "B"],
    ["D", "C"],
]

CASES = (
    ("empty grid", [], ["A", "B"], []),
    ("empty row", [[]], ["A"], []),
    ("no words", EXAMPLE_BOARD, [], []),
    (
        "example board",
        EXAMPLE_BOARD,
        ["oath", "pea", "eat", "rain"],
        ["oath", "eat"],
    ),
    (
        "keeps the requested order",
        EXAMPLE_BOARD,
        ["eat", "rain", "oath", "pea"],
        ["eat", "oath"],
    ),
    ("repeated word", EXAMPLE_BOARD, ["eat", "eat"], ["eat", "eat"]),
    ("every word missing", EXAMPLE_BOARD, ["pea", "rain", "zzz"], []),
    (
        "fact grid",
        FACT_GRID,
        ["FACT", "LEAF", "FACE", "CASTLE", "FAST"],
        ["FACT", "LEAF", "CASTLE"],
    ),
    ("cannot reuse a cell", [["A"]], ["A", "AA"], ["A"]),
    ("snake", SNAKE_GRID, ["AB", "ABCD", "ABCA", "DC"], ["AB", "ABCD", "DC"]),
    ("single cell missing", [["A"]], ["B"], []),
)


def search(function, grid, words):
    copied = [row.copy() for row in grid]
    try:
        return function(copied, words), copied
    except Exception as error:
        return type(error).__name__, copied


def found_words(actual):
    if isinstance(actual, list):
        return sorted(set(actual))
    return actual


def format_grid(grid):
    if not grid:
        return "(empty grid)"
    if not grid[0]:
        return "(empty row)"
    return "\n".join(" ".join(row) for row in grid)


class TestNaiveMultipleWordSearch(unittest.TestCase):
    def test_returns_the_words_that_have_a_valid_path(self):
        for name, grid, words, expected in CASES:
            with self.subTest(name=name, words=words):
                actual, _grid_after = search(naiveMutipleWordSearch, grid, words)
                self.assertEqual(actual, expected)

    def test_does_not_modify_the_grid(self):
        original = [row.copy() for row in EXAMPLE_BOARD]
        _actual, grid_after = search(
            naiveMutipleWordSearch,
            EXAMPLE_BOARD,
            ["oath", "pea", "eat", "rain"],
        )
        self.assertEqual(grid_after, original)


class TestOptimalMultipleWordSearch(unittest.TestCase):
    def test_returns_each_found_word_once(self):
        for name, grid, words, expected in CASES:
            with self.subTest(name=name, words=words):
                actual, _grid_after = search(optimalMutipleWordSearch, grid, words)
                self.assertEqual(found_words(actual), found_words(expected))

    def test_does_not_modify_the_grid(self):
        original = [row.copy() for row in EXAMPLE_BOARD]
        _actual, grid_after = search(
            optimalMutipleWordSearch,
            EXAMPLE_BOARD,
            ["oath", "pea", "eat", "rain"],
        )
        self.assertEqual(grid_after, original)


def show_cases():
    print("Multiple word search")
    print("Each word moves up, down, left, or right and does not reuse a cell.")
    print()

    for number, (name, grid, words, expected) in enumerate(CASES, start=1):
        naive, _grid_after = search(naiveMutipleWordSearch, grid, words)
        optimal, _grid_after = search(optimalMutipleWordSearch, grid, words)
        naive_status = "ok" if naive == expected else "FAIL"
        optimal_status = "ok" if found_words(optimal) == found_words(expected) else "FAIL"
        print(f"[{number}] {name}")
        print(format_grid(grid))
        print(f"words:    {words}")
        print(f"expected: {expected}")
        print(f"naive:    {naive} ({naive_status})")
        print(f"optimal:  {optimal} ({optimal_status})")
        print()


if __name__ == "__main__":
    show_cases()
