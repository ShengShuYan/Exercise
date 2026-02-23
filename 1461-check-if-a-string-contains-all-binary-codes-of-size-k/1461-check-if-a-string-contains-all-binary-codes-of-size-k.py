class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2 ** k
        len_s = len(s)
        if len_s <  k:
            return False

        sub_sub = deque()
        
        for z in range(k):
            sub_sub.append(s[z])

        subset = {''.join(sub_sub)}

        for j in range(len_s - k):
            sub_sub.popleft()
            sub_sub.append(s[k+j])
            subset.add(''.join(sub_sub))

        if len(subset) == 2 ** k:
            return True

        return False     