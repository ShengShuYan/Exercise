class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1 = []
        l2 = []
        eq = 0
        for c in nums:
            if c < pivot:
                l1.append(c)
            elif c > pivot:
                l2.append(c)
            else:
                eq += 1

        return l1 + [pivot] * eq + l2
        