// https://leetcode.com/problems/design-add-and-search-words-data-structure

from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        """Returns if the word is in the data structure.
        A word can contain the dot[.] character to represent the
        letter."""
        for other in self.words[len(word)]:
            any_mismatch = any(word[x] != '.' and word[x] != other[x] for x in range(len(word)))
            if not any_mismatch:
                return True
                
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)