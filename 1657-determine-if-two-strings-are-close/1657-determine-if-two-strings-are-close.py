from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1, d2 = Counter(word1), Counter(word2)

        return d1.keys() == d2.keys() and Counter(d1.values()) == Counter(d2.values())

        