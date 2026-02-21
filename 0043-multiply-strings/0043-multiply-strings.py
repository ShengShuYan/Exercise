class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        result = [0] * (l1 + l2)

        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1, p2 = i + j, i +j + 1
                tot = mul + result[p2]

                result[p2] = tot % 10
                result[p1] += tot // 10

        return ''.join(map(str, result)).lstrip('0') or '0'

        