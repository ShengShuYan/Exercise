import bisect

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        m = k - 1
        
        window = sorted(nums[1:dist+2])
        current_sum = sum(window[:m])
        ans = nums[0] + current_sum
        
        for i in range(1, n - dist - 1):
            out_val = nums[i]
            idx = bisect.bisect_left(window, out_val)
            
            if idx < m:
                current_sum -= out_val
                if len(window) > m:
                    current_sum += window[m]
            window.pop(idx)
            
            in_val = nums[i + dist + 1]
            idx_in = bisect.bisect_left(window, in_val)
            
            if idx_in < m:
                current_sum += in_val
                if len(window) >= m:
                    current_sum -= window[m-1]
            bisect.insort(window, in_val)
            
            ans = min(ans, nums[0] + current_sum)
            
        return ans