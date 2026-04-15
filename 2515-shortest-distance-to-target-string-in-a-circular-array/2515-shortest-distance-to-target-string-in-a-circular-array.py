class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        dif = 0
        N = len(words)
        while dif < N:
            if words[(startIndex+dif)%N] == target or words[(startIndex-dif+N)%N] == target:
                break
            dif += 1
        if dif == N:
            return -1
        else:
            return dif
        