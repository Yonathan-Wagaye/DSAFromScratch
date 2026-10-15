"""
Given a list of words how can we efficently search for words that start with a given prefix?
Example:
Input: words = ["apple", "app", "apples", "applesauce"]
Prefix: "app"
Output: ["apple", "app", "apples", "applesauce"]
The solution is using a Trie data structure
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isWord = True

    def search(self, word) -> bool:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.isWord

    def prefixSearch(self, prefix) -> bool:
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return True
