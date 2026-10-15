import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Backtracking"))

from singleCharSearch import (
    singleCharSearchGraphDFS,
    singleCharSearchLoopVariation,
    singleCharSearchRecursiveVariant,
)

FUNCTIONS = (
    ("graph dfs", singleCharSearchGraphDFS),
    ("loop", singleCharSearchLoopVariation),
    ("recursive", singleCharSearchRecursiveVariant),
)

# Every case runs every function. The absent grid stays at 12 x 12 because the
# right-and-down search repeats overlapping paths and does not finish on the
# larger grids used by the other cases.
CASES = (
    {
        "id": "1",
        "name": "First cell",
        "rows": 500,
        "cols": 500,
        "target": "Z",
        "at": (0, 0),
        "repeats": 5,
        "recursion_limit": None,
    },
    {
        "id": "2",
        "name": "Last cell",
        "rows": 40,
        "cols": 40,
        "target": "Z",
        "at": (39, 39),
        "repeats": 3,
        "recursion_limit": 2000,
    },
    {
        "id": "3",
        "name": "Absent",
        "rows": 12,
        "cols": 12,
        "target": "Z",
        "at": None,
        "repeats": 1,
        "recursion_limit": None,
    },
)


def make_grid(rows, cols, target, at):
    grid = [["A" for _ in range(cols)] for _ in range(rows)]
    if at is not None:
        row, col = at
        grid[row][col] = target
    return grid


def time_function(function, grid, target, repeats):
    best = None
    result = None

    for _ in range(repeats):
        start = time.perf_counter()
        result = function(grid, target)
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


def case_label(case):
    return f"[{case['id']}] {case['name']}"


def target_location(case):
    if case["at"] is None:
        return "not in the grid"
    return f"at {case['at']}"


def print_cases():
    print("Cases")
    for case in CASES:
        runs = "1 run" if case["repeats"] == 1 else f"fastest of {case['repeats']}"
        print(
            f"  {case_label(case):<16}"
            f"{case['rows']:>4} x {case['cols']:<4}"
            f"  target {case['target']!r} {target_location(case):<16}"
            f"  {runs}"
        )


def print_results(measurements):
    headers = ["Function", *[case_label(case) for case in CASES]]
    rows = []

    for name, _function in FUNCTIONS:
        row = [name]
        for case in CASES:
            result, elapsed = measurements[(case["id"], name)]
            row.append(f"{str(result):<5} {format_time(elapsed):>8}")
        rows.append(row)

    widths = [
        max(len(headers[column]), *(len(row[column]) for row in rows))
        for column in range(len(headers))
    ]

    def render(values):
        return "  ".join(value.ljust(widths[index]) for index, value in enumerate(values))

    print()
    print("Results")
    print(render(headers))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print(render(row))


def main():
    measurements = {}
    previous_limit = sys.getrecursionlimit()

    print("Single-character search")
    print()
    print_cases()

    try:
        for case in CASES:
            if case["recursion_limit"] is not None:
                sys.setrecursionlimit(case["recursion_limit"])
            grid = make_grid(case["rows"], case["cols"], case["target"], case["at"])
            for name, function in FUNCTIONS:
                measurements[(case["id"], name)] = time_function(
                    function,
                    grid,
                    case["target"],
                    case["repeats"],
                )
            sys.setrecursionlimit(previous_limit)
    finally:
        sys.setrecursionlimit(previous_limit)

    print_results(measurements)
    print()


if __name__ == "__main__":
    main()
