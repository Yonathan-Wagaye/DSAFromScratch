import unittest

from Backtracking.singleWordSearch import singleWordSearch

EXAMPLE_GRID = [
    ["T", "C", "O", "E"],
    ["E", "A", "F", "C"],
    ["L", "T", "S", "A"],
]

SNAKE_GRID = [
    ["A", "B"],
    ["D", "C"],
]

# A valid path moves only up, down, left, or right and never reuses a cell.
CASES = (
    ("empty grid", [], "A", False),
    ("empty row", [[]], "A", False),
    ("single cell found", [["A"]], "A", True),
    ("single cell missing", [["A"]], "B", False),
    ("single letter in example", EXAMPLE_GRID, "F", True),
    ("fact", EXAMPLE_GRID, "FACT", True),
    ("castle", EXAMPLE_GRID, "CASTLE", True),
    ("leaf", EXAMPLE_GRID, "LEAF", True),
    ("cast", EXAMPLE_GRID, "CAST", True),
    ("cats", EXAMPLE_GRID, "CATS", True),
    ("taco", EXAMPLE_GRID, "TACO", True),
    ("face uses a diagonal", EXAMPLE_GRID, "FACE", False),
    ("fast uses a diagonal", EXAMPLE_GRID, "FAST", False),
    ("word missing", EXAMPLE_GRID, "ZZZ", False),
    ("cannot reuse the only cell", [["A"]], "AA", False),
    ("snake uses left", SNAKE_GRID, "ABCD", True),
    ("snake cannot return to A", SNAKE_GRID, "ABCA", False),
)


def search(grid, word):
    copied = [row.copy() for row in grid]
    try:
        return singleWordSearch(copied, word), copied
    except RecursionError:
        return "RecursionError", copied


def format_grid(grid):
    if not grid:
        return "(empty grid)"
    if not grid[0]:
        return "(empty row)"
    return "\n".join(" ".join(row) for row in grid)


class TestSingleWordSearch(unittest.TestCase):
    def test_finds_only_valid_paths(self):
        for name, grid, word, expected in CASES:
            with self.subTest(name=name, word=word):
                actual, _grid_after = search(grid, word)
                self.assertEqual(actual, expected)

    def test_does_not_modify_the_grid(self):
        original = [row.copy() for row in EXAMPLE_GRID]
        _actual, grid_after = search(EXAMPLE_GRID, "FACT")
        self.assertEqual(grid_after, original)


def show_cases():
    print("Single word search")
    print("A match moves up, down, left, or right and does not reuse a cell.")
    print()

    for number, (name, grid, word, expected) in enumerate(CASES, start=1):
        actual, _grid_after = search(grid, word)
        status = "ok" if actual == expected else "FAIL"
        print(f"[{number}] {name}")
        print(format_grid(grid))
        print(f"word:     {word}")
        print(f"expected: {expected}")
        print(f"actual:   {actual}")
        print(status)
        print()


if __name__ == "__main__":
    show_cases()
