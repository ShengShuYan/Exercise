class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        t = False
        for c in s[::-1]: 
            if t and c == ' ':
                break
            elif c != ' ':
                t = True
                l += 1
        return l