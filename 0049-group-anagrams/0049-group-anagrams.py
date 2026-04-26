from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            cou = [0] * 26
            for c in s:
                cou[ord(c) - ord('a')]+= 1
            ans[tuple(cou)].append(s)
        return list(ans.values())

        