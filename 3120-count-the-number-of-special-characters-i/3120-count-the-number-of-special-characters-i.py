class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = [0] * 26
        ans = 0
        seen = set()
        for c in word:
            if c in seen:
                continue
            if 'a' <= c <='z':
                count[ord(c) - ord('a')] += 1
            else:
                count[ord(c) - ord('A')] += 1
            seen.add(c)

        for i in count:
            if i > 1:
                ans += 1
        return ans
        