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

from Backtracking.singleWordSearch import singleWordSearch


def naiveMutipleWordSearch(grid, words):
    result = []

    for word in words:
        if singleWordSearch(grid, word):
            result.append(word)
    return result
