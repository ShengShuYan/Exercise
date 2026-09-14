def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        common = gcd(l1, l2)
        
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:common]
        
        
        