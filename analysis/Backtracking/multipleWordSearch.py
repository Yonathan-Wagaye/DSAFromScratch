import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Backtracking.multipleWordSearch import naiveMutipleWordSearch


def blank_grid(rows, cols, fill):
    return [[fill for _ in range(cols)] for _ in range(rows)]


EXAMPLE_BOARD = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]


CASES = (
    {
        "id": "1",
        "name": "Example",
        "detail": "4 words, 2 found",
        "rows": 4,
        "cols": 4,
        "repeats": 5,
        "grid": EXAMPLE_BOARD,
        "words": ["oath", "pea", "eat", "rain"],
    },
    {
        "id": "2",
        "name": "First word",
        "detail": "1 word at (0, 0)",
        "rows": 30,
        "cols": 30,
        "repeats": 5,
        "grid": blank_grid(30, 30, "B"),
        "words": ["A"],
    },
    {
        "id": "3",
        "name": "Mixed list",
        "detail": "6 words, 3 found",
        "rows": 15,
        "cols": 15,
        "repeats": 3,
        "grid": blank_grid(15, 15, "A"),
        "words": ["A", "AA", "AAA", "B", "C", "Z"],
    },
    {
        "id": "4",
        "name": "All missing",
        "detail": "40 words, none found",
        "rows": 20,
        "cols": 20,
        "repeats": 3,
        "grid": blank_grid(20, 20, "B"),
        "words": ["A"] * 40,
    },
    {
        "id": "5",
        "name": "Repeated misses",
        "detail": "8 long words, none found",
        "rows": 5,
        "cols": 5,
        "repeats": 1,
        "grid": blank_grid(5, 5, "A"),
        "words": ["A" * 7 + "Z"] * 8,
    },
)

CASES[1]["grid"][0][0] = "A"


def time_search(grid, words, repeats):
    best = None
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = naiveMutipleWordSearch(grid, words)
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
    print("Multiple word search")
    print("Function: naiveMutipleWordSearch")
    print()

    headers = ("Case", "Grid", "Words", "Found", "Time")
    rows = []
    for case in CASES:
        result, elapsed = time_search(case["grid"], case["words"], case["repeats"])
        runs = "1 run" if case["repeats"] == 1 else f"fastest of {case['repeats']}"
        found = len(result) if isinstance(result, list) else result
        rows.append(
            (
                f"[{case['id']}] {case['name']}",
                f"{case['rows']} x {case['cols']}",
                case["detail"],
                str(found),
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
