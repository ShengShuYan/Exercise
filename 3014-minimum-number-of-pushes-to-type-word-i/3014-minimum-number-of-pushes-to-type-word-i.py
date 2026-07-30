class Solution:
    def minimumPushes(self, word: str) -> int: 
        L = len(word)
        ans = L
        while L > 8:
            L -= 8
            ans += L
        return ans