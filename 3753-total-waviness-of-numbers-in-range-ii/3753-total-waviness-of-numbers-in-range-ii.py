from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n <= 0: return 0
            s = str(n)
            
            # (count, total_waviness)
            @cache
            def dfs(pos, prev1, prev2, tight, is_zero):
                if pos == len(s):
                    return 1, 0
                
                res_count = 0
                res_sum = 0
                limit = int(s[pos]) if tight else 9
                
                for digit in range(limit + 1):
                    new_tight = tight and (digit == limit)
                    
                    if is_zero:
                        if digit == 0:
                            # 依然是前导零
                            c, s_val = dfs(pos + 1, -1, -1, new_tight, True)
                            res_count += c
                            res_sum += s_val
                        else:
                            # 填入第一个有效数字
                            c, s_val = dfs(pos + 1, digit, -1, new_tight, False)
                            res_count += c
                            res_sum += s_val
                    else:
                        # 核心：判断峰谷
                        is_waviness = 0
                        if prev2 != -1:
                            if (prev2 < prev1 and digit < prev1) or (prev2 > prev1 and digit > prev1):
                                is_waviness = 1
                        
                        c, s_val = dfs(pos + 1, digit, prev1, new_tight, False)
                        
                        # 重要修正：每一条子路径的 waviness 都要累加
                        # 产生的 waviness = (当前形成的峰谷) * (当前路径下有效数字的个数) + 下层传回来的总和
                        res_count += c
                        res_sum += (is_waviness * c) + s_val
                        
                return res_count, res_sum
            
            return dfs(0, -1, -1, True, True)[1]

        return solve(num2) - solve(num1 - 1)