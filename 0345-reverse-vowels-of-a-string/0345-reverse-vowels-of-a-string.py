class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        ans = [c for c in s]
        lst = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        r = len(s) - 1
        while l < r:
            while s[l] not in lst and l < r:
                l += 1
            if l == r: break            
            while s[r] not in lst and l < r:
                r -= 1
            if l == r: break            
            ans[l] = s[r]
            ans[r] = s[l]
            l += 1
            r -= 1
        return ''.join(ans)
        