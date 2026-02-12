class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        L = 0
        smap = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
        }

        l = [0] * 26

        for c in s:
            l[smap[c]] += 1

        for i in range(n):           
            if i != 0:
                l[smap[s[i-1]]] -= 1
            num = set(l)
            if (len(num) == 2 and 0 in num) or (len(num) == 1 and not(0 in num)):
                    cur = n - i
                    L = max(L, cur)
                    break
            l1 = l[:]    
            for j in range(n-1, i-1, -1):
                
                if j != n-1:
                    l1[smap[s[j+1]]] -= 1   
                num = set(l1)
                if (len(num) == 2 and 0 in num) or (len(num) == 1 and 0 not in num):
                    cur = j - i + 1
                    L = max(L, cur)
                    break
                          
        return L


        