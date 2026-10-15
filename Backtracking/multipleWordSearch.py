"""
Given a matrix of characters and a list of words, find all words in the matrix.

Words can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Explanation:
The word "oath" can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The word "eat" can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The word "rain" cannot be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
"""

from ast import List

from Backtracking.singleWordSearch import singleWordSearch
from Trees.Tire import Trie, TrieNode


def naiveMutipleWordSearch(grid, words):
    result = []

    for word in words:
        if singleWordSearch(grid, word):
            result.append(word)
    return result


def optimalMutipleWordSearch(grid, words):
    if not grid or not grid[0]:
        return []

    ROW, COL = len(grid), len(grid[0])
    result, visited = set(), set()
    trie = Trie()
    trie.insertFromArray(words)

    def backtrack(row, col, node: TrieNode, word) -> List:
        if (
            min(row, col) < 0
            or row >= ROW
            or col >= COL
            or (row, col) in visited
            or grid[row][col] not in node.children
        ):
            return

        visited.add((row, col))
        word += grid[row][col]
        node = node.children[grid[row][col]]

        if node.isWord:
            result.add(word)

        dxns = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for x, y in dxns:
            backtrack(row + x, col + y, node, word)
        visited.remove((row, col))

    for i in range(ROW):
        for j in range(COL):
            backtrack(i, j, trie.root, "")
    return list(result)
