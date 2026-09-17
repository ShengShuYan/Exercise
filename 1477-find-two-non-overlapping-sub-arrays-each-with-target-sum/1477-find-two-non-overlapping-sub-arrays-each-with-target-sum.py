class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l = len(arr)
        dp = [float('inf')] * l

        start = 0
        cur_sum = 0
        ans = float('inf')
        min_l = float('inf')
        
        for end in range(l):
            v = arr[end]
            
            while cur_sum + v > target:
                cur_sum -= arr[start]
                start += 1
            
            cur_sum += v
            
            if cur_sum == target:
                cur_l = end - start + 1
                ans = min(ans, dp[start-1] + cur_l)
                min_l = min(min_l, cur_l)
            
            dp[end] = min_l

        return ans if ans != float('inf') else -1