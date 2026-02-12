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
        for i in range(n):
            l = [0] * 26
            for j in range(i,n):
                l[smap[s[j]]] += 1
                num = set(l)
                if (len(num) == 2 and 0 in num) or (len(num) == 1 and not(0 in num)):
                    cur = j - i + 1
                    L = max(L, cur)

        return L


        