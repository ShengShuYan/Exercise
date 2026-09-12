class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ans = []
        if l1 > l2:
            for i in range(l2):
                ans.append(word1[i])
                ans.append(word2[i])
            return ''.join(ans)+word1[l2:]
        else:
            for i in range(l1):
                ans.append(word1[i])
                ans.append(word2[i])
            return ''.join(ans)+word2[l1:]
        