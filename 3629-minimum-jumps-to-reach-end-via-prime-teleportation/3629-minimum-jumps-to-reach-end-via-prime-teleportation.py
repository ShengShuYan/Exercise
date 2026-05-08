from collections import deque, defaultdict

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        max_val = max(nums)
        # 1. 预处理：埃氏筛获取最小质因数，优化质因数分解
        min_prime = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if min_prime[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if min_prime[j] == j:
                        min_prime[j] = i
        
        # 2. 建立 质数 -> 索引列表 的映射
        prime_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = min_prime[temp]
                prime_to_indices[p].append(i)
                while temp % p == 0: # 移除所有该质因子
                    temp //= p
        
        # 3. BFS
        queue = deque([(0, 0)]) # (index, steps)
        visited_idx = {0}
        visited_prime = set()
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
            
            # 情况 A: 相邻跳跃
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_idx:
                    visited_idx.add(next_idx)
                    queue.append((next_idx, steps + 1))
            
            # 情况 B: 质数传送
            # 只有当前位置的数是质数时才能传送
            val = nums[curr_idx]
            # 这里根据题目要求：如果 nums[i] 是质数 p，跳到所有 p 的倍数
            # 注意：只有 nums[curr_idx] 本身是质数时才触发
            if min_prime[val] == val and val > 1:
                p = val
                if p not in visited_prime:
                    for next_idx in prime_to_indices[p]:
                        if next_idx not in visited_idx:
                            visited_idx.add(next_idx)
                            queue.append((next_idx, steps + 1))
                    visited_prime.add(p) # 该质数所有倍数已入队，标记避免重复计算

        return -1
