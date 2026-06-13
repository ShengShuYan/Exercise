class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            a = 0
            for c in word:
                a += weights[ord(c) - ord('a')]
            ans.append(chr(122-a%26))

        return ''.join(ans)
            
        