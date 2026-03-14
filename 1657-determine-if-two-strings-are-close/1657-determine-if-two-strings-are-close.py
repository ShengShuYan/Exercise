from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = Counter(word1)
        d2 = Counter(word2)

        counter1 = sorted(d1.values())
        counter2 = sorted(d2.values())

        item1 = sorted(d1.keys())
        item2 = sorted(d2.keys())
        return counter1 == counter2 and item1 == item2

        