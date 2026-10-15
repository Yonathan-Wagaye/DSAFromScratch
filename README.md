# DSA

Python practice for data structures, algorithms, and LeetCode-style problems.

## Layout

- `Backtracking/`, `Heaps/`, and `Trees/` hold the solutions.
- `tests/` holds the unit tests.
- `analysis/` holds timing scripts, grouped the same way as the solutions.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Run a solution

```bash
./run Heaps/PriorityQueue.py
./run PriorityQueue
./run singleWordSearch
```

`./run` with no arguments lists the solution files.

## Tests

```bash
./run test
./run test-show
```

`./run test` runs the unit tests. `./run test-show` prints the small word-search cases with the expected result and the actual result.

## Timing

```bash
./run analyze Backtracking
./run analyze Backtracking singleCharSearch
./run analyze Backtracking singleWordSearch
./run analyze Backtracking multipleWordSearch
```

`./run analyze` with only a section name runs every timing script in that section. Adding a file name runs that script alone.
