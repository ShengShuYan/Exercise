class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        for c1, c2 in zip(word1, word2):
            merged.append(c1)
            merged.append(c2)
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])
        return ''.join(merged)