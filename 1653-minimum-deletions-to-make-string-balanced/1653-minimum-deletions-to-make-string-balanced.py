class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = len(s)
        current = s.count('a')
        count = min(current, count)
        if current == 0 or s.count('b') == 0:
            return 0
        if s[0] == 'a':
            current -= 1
            count = min(current, count)
        for i in range(1, len(s)):
            if s[i-1] == 'a' and s[i] == 'a':
                current -= 1
                count = min(current, count)
            elif s[i-1] == 'b' and s[i] == 'b':
                current += 1
        return count
        