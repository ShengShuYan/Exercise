from itertools import combinations

class Solution:
    def solve2(self, s, c1, c2, noc):
        seen = {0: -1}
        diff = 0
        L = 0

        for i, c in enumerate(s):
            if c == noc:
                seen = {0: i}
                diff = 0
            else:
                if c == c1:
                    diff -= 1
                elif c == c2:
                    diff += 1
                
                if diff in seen:
                    L = max(L, i - seen[diff])
                else:
                    seen[diff] = i

        return L

    def solve3(self, s):
        seen = {(0, 0): -1}
        a = b = c = 0
        L = 0
        for i, ch in enumerate(s):
            if ch == 'a': a += 1
            elif ch == 'b': b += 1
            else: c += 1
            
            state = (b - a, c - a)
            if state in seen:
                L = max(L, i - seen[state])
            else:
                seen[state] = i

        return L

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        L = 1
        
        count1 = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count1 += 1
            else:
                count1 = 1
            if L < count1:
                L = count1
        
        count2_1 = self.solve2( s, 'a', 'b', 'c')
        count2_2 = self.solve2(s, 'b', 'c', 'a')
        count2_3 = self.solve2(s, 'c', 'a', 'b')

        count3 = self.solve3(s)

        L = max(L, count2_1, count2_2, count2_3, count3)

        return L