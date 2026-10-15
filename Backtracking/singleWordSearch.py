"""
Given a 2D grid of characters and a target word, return true if the word is found in the grid with a valid path without revisiting the same cell in a single path, false otherwise.
The search should use backtracking to find the target word.

Example:
grid = [
    ['T', 'C', 'O', 'E'],
    ['E', 'A', 'F', 'C'],
    ['L', 'T', 'S', 'A']
]
target = 'FACT'
output: true

Here are other examples of valid paths that could produce words in the English language:
FACT: F(1,2) → A(1,1) → C(0,1) → T(0,0)
CASTLE: C(1,3) → A(2,3) → S(2,2) → T(2,1) → L(2,0) → E(1,0)
LEAF: L(2,0) → E(1,0) → A(1,1) → F(1,2)
CAST: C(1,3) → A(2,3) → S(2,2) → T(2,1)
CATS: C(0,1) → A(1,1) → T(2,1) → S(2,2)
TACO: T(2,1) → A(1,1) → C(0,1) → O(0,2)
"""


def singleWordSearch(grid, target):
    if not grid or not grid[0] or not target:
        return False

    ROW, COL = len(grid), len(grid[0])

    visited = set()
    n = len(target)

    def backtrack(row, col, wordIndex):
        if wordIndex == n:
            return True
        if min(row, col) < 0 or row >= ROW or col >= COL:
            return False
        if (row, col) in visited:
            return False
        if grid[row][col] != target[wordIndex]:
            return False

        visited.add((row, col))
        dxns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dxn in dxns:
            if backtrack(row + dxn[0], col + dxn[1], wordIndex + 1):
                return True
        visited.remove((row, col))
        return False

    for i in range(ROW):
        for j in range(COL):
            if backtrack(i, j, 0):
                return True
    return False
