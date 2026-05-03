class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for _ in range(n):
            ans.append(nums[_])
            ans.append(nums[n+_])
        return ans
        