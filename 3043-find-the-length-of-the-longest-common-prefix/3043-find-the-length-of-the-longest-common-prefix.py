class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set2 = set()
        for i in arr2:
            while i > 0:
                set2.add(i)
                i = i // 10

        ans = 0
        
        for j in arr1:
            while j > 0:
                if j in set2:
                    ans = max(ans, len(str(j)))
                    break
                j = j // 10

        return ans

        