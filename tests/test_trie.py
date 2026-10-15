import unittest

from Trees.Tire import Trie


class TestTrie(unittest.TestCase):
    def test_search_finds_an_inserted_word(self):
        trie = Trie()
        trie.insert("apple")

        self.assertTrue(trie.search("apple"))

    def test_search_rejects_a_word_that_was_not_inserted(self):
        trie = Trie()
        trie.insert("apple")

        self.assertFalse(trie.search("orange"))

    def test_search_rejects_a_proper_prefix(self):
        trie = Trie()
        trie.insert("apple")

        self.assertFalse(trie.search("app"))

    def test_search_finds_a_shorter_word_that_shares_a_prefix(self):
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")

        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("apple"))

    def test_search_is_case_sensitive(self):
        trie = Trie()
        trie.insert("App")

        self.assertTrue(trie.search("App"))
        self.assertFalse(trie.search("app"))

    def test_search_handles_a_single_character(self):
        trie = Trie()
        trie.insert("a")

        self.assertTrue(trie.search("a"))
        self.assertFalse(trie.search("b"))

    def test_empty_trie_rejects_every_search(self):
        trie = Trie()

        self.assertFalse(trie.search("apple"))
        self.assertFalse(trie.search(""))

    def test_prefix_search_matches_the_example_words(self):
        trie = Trie()
        for word in ("apple", "app", "apples", "applesauce"):
            trie.insert(word)

        self.assertTrue(trie.prefixSearch("app"))
        self.assertTrue(trie.prefixSearch("apple"))
        self.assertTrue(trie.prefixSearch("applesauce"))
        self.assertFalse(trie.prefixSearch("orange"))
        self.assertFalse(trie.prefixSearch("apt"))

    def test_prefix_search_distinguishes_diverging_words(self):
        trie = Trie()
        trie.insert("cat")
        trie.insert("car")

        self.assertTrue(trie.prefixSearch("ca"))
        self.assertTrue(trie.prefixSearch("cat"))
        self.assertTrue(trie.prefixSearch("car"))
        self.assertFalse(trie.prefixSearch("cap"))
        self.assertFalse(trie.search("ca"))

    def test_prefix_search_rejects_a_prefix_longer_than_the_word(self):
        trie = Trie()
        trie.insert("app")

        self.assertFalse(trie.prefixSearch("apple"))

    def test_empty_prefix_matches(self):
        trie = Trie()
        trie.insert("apple")

        self.assertTrue(trie.prefixSearch(""))


if __name__ == "__main__":
    unittest.main()
