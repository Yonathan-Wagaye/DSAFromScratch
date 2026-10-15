"""
Given a 2D grid of characters and a traget character t, return true if t is found in the grid, false otherwise.

The searh should use backtracking to find the target character.

Example:
grid = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
target = 'D'
output: true
Explanation:
The target character 'D' is found in the grid at the position (2, 1).
"""


def singleCharSearchGraphDFS(
    grid, target
):  # Time complexity: O(n * m) where n is the number of rows and m is the number of columns
    if not grid or not grid[0]:  # empty grid
        return False
    visited = set()  # contain a tuple of (row, col) for each visited cell
    ROW, COL = len(grid), len(grid[0])

    def dfs(row, col):
        # base case 1 out of bounds
        if min(row, col) < 0 or row >= ROW or col >= COL:
            return False
        # base case 2 cell already visited
        if (row, col) in visited:
            return False
        # base case 3 cell matches target
        if grid[row][col] == target:
            return True

        # recursive cases
        visited.add((row, col))
        dxns = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dxn in dxns:
            if dfs(row + dxn[0], col + dxn[1]):
                return True
        return False

    return dfs(0, 0)


def singleCharSearchLoopVariation(
    grid, target
):  # Time complexity: O(n * m) where n is the number of rows and m is the number of columns
    if not grid or not grid[0]:
        return False

    ROW, COL = len(grid), len(grid[0])

    for i in range(ROW):
        for j in range(COL):
            if grid[i][j] == target:
                return True
    return False


def singleCharSearchRecursiveVariant(
    grid, target
):  # Time complexity: O(2^n) where n is the number of cells in the grid
    if not grid or not grid[0]:
        return False

    ROW, COL = len(grid), len(grid[0])

    def recursiveSearch(row, col):
        if min(row, col) < 0 or row >= ROW or col >= COL:
            return False

        if grid[row][col] == target:
            return True

        if (row, col) == (ROW - 1, COL - 1):
            return False

        dxns = [(0, 1), (1, 0)]
        for dxn in dxns:
            if recursiveSearch(row + dxn[0], col + dxn[1]):
                return True

        return False

    return recursiveSearch(0, 0)
