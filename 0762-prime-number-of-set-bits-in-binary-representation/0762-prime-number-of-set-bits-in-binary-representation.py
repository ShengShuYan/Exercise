class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            count += self.is_prime(i)

        return count

    def is_prime(self, a: int) -> int:
        a_count = bin(a).count('1')
        if a_count <= 1:
            return 0
        if a_count <= 3:
            return 1
        if a_count % 2 == 0 or a_count % 3 == 0:
            return 0

        i = 5
        while i * i <= a_count:
            if a_count % i == 0 or a_count % (i+2) == 0:
                return 0
            i += 6

        return 1


            

        