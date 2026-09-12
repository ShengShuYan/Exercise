class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for ch1, ch2 in zip(word1, word2):
            ans.append(ch1)
            ans.append(ch2)
        l = min(len(word1), len(word2))
        ans.append(word1[l:])
        ans.append(word2[l:])
        return ''.join(ans)
        