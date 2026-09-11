class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        maps = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0
        }
        n = len(digits)
        ans = 0
        for d in digits:
            maps[d] += 1
        for even in [0, 2, 4, 6, 8]:
            if maps[even] == 0:
                continue
            maps[even] -= 1
            for key in maps:
                if key == 0 or maps[key] == 0:
                    continue
                maps[key] -= 1
                ans += sum(val > 0 for val in maps.values())
                maps[key] += 1
            maps[even] += 1

        return ans



        