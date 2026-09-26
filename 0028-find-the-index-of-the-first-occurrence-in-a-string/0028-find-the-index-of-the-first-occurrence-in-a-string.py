class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j, l1, l2 = 0, 0, len(haystack), len(needle)
        while i < l1 and j < l2:
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
            else:
                i += 1
                j += 1
            if j == l2:
                return i - j
        return -1