import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Backtracking"))

from singleWordSearch import singleWordSearch


def blank_grid(rows, cols, fill):
    return [[fill for _ in range(cols)] for _ in range(rows)]


def snake_grid(rows, cols):
    """A 4-direction path of A's that visits every cell."""
    grid = blank_grid(rows, cols, "B")
    for row in range(rows):
        columns = range(cols) if row % 2 == 0 else range(cols - 1, -1, -1)
        for col in columns:
            grid[row][col] = "A"
    return grid


CASES = (
    {
        "id": "1",
        "name": "First cell",
        "detail": "word 'A' at (0, 0)",
        "rows": 40,
        "cols": 40,
        "repeats": 5,
        "grid": blank_grid(40, 40, "B"),
        "word": "A",
    },
    {
        "id": "2",
        "name": "Last cell",
        "detail": "word 'A' at (39, 39)",
        "rows": 40,
        "cols": 40,
        "repeats": 5,
        "grid": blank_grid(40, 40, "B"),
        "word": "A",
    },
    {
        "id": "3",
        "name": "Full path",
        "detail": "225-letter snake from (0, 0)",
        "rows": 15,
        "cols": 15,
        "repeats": 3,
        "grid": snake_grid(15, 15),
        "word": "A" * (15 * 15),
    },
    {
        "id": "4",
        "name": "Absent",
        "detail": "8-letter word, no full path",
        "rows": 5,
        "cols": 5,
        "repeats": 1,
        "grid": blank_grid(5, 5, "A"),
        "word": "A" * 7 + "Z",
    },
)

CASES[0]["grid"][0][0] = "A"
CASES[1]["grid"][39][39] = "A"


def time_search(grid, word, repeats):
    best = None
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = singleWordSearch(grid, word)
        elapsed = time.perf_counter() - start
        if best is None or elapsed < best:
            best = elapsed
    return result, best


def format_time(seconds):
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f} µs"
    if seconds < 1:
        return f"{seconds * 1000:.1f} ms"
    return f"{seconds:.2f} s"


def main():
    print("Single word search")
    print("Function: singleWordSearch")
    print()

    headers = ("Case", "Grid", "Word", "Result", "Time")
    rows = []
    for case in CASES:
        result, elapsed = time_search(case["grid"], case["word"], case["repeats"])
        runs = "1 run" if case["repeats"] == 1 else f"fastest of {case['repeats']}"
        rows.append(
            (
                f"[{case['id']}] {case['name']}",
                f"{case['rows']} x {case['cols']}",
                case["detail"],
                str(result),
                f"{format_time(elapsed)} ({runs})",
            )
        )

    widths = [
        max(len(headers[column]), *(len(row[column]) for row in rows))
        for column in range(len(headers))
    ]

    def render(values):
        return "  ".join(value.ljust(widths[index]) for index, value in enumerate(values))

    print(render(headers))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print(render(row))
    print()


if __name__ == "__main__":
    main()
