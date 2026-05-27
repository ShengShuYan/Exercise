class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cmap = [0] * 26
        ans = 0
        for c in word:
            if 'a' <= c <= 'z':
                if cmap[ord(c) - ord('a')] == 0:
                    cmap[ord(c) - ord('a')] += 1
                elif cmap[ord(c) - ord('a')] == 2:
                    cmap[ord(c) - ord('a')] += 1
            else:
                if cmap[ord(c) - ord('A')] == 1:
                    cmap[ord(c) - ord('A')] += 1
                elif cmap[ord(c) - ord('A')] == 0:
                    cmap[ord(c) - ord('A')] -= 1
        for z in cmap:
            if z == 2:
                ans += 1

        return ans
        